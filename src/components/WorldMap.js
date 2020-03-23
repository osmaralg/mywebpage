import React, { Component } from 'react'
import 'assets/css/App.css'
import worlddata from './world'
import { geoMercator, geoPath } from 'd3-geo'
import { range, sum } from 'd3-array'
import { scaleThreshold } from 'd3-scale'
import { geoCentroid } from 'd3-geo'
import BarChart from 'components/BarChart.js'
import { select } from 'd3-selection'
import ReactDOM from 'react-dom'; // you used 'react-dom' as 'ReactDOM'

class CountryLabel extends Component {
  render(){
    return <h1>{this.props.label}</h1>
  }
}

class WorldMap extends Component {

  render() {

    const node = this.node
    const projection = geoMercator()
      .scale(120)
      .translate([430,250])
    const pathGenerator = geoPath().projection(projection)
    const countries = this.props.data
      .map((d,i) => <svg><path
        key={"path" + i}
        d={pathGenerator(d)}
        onClick={() => {
          this.props.onHover(d)
          const element =  <circle cx={projection(geoCentroid(d))[0]} cy={projection(geoCentroid(d))[1]} r="1" 
            style={{fill: this.props.hoverElement === d.id ? "#FCBC34" : "#FF0000", stroke: "black", strokeOpacity: 0.5 }} />
          ReactDOM.render(element, document.getElementById('line-div'));

          }
        }
        style={{fill: this.props.hoverElement === d.id ? "#FCBC34" : this.props.colorScale(d.launchday), stroke: "black", strokeOpacity: 0.5 }}
        className="countries"
      />
     
      </svg>
      )



    return <svg id="world-svg" ref="world-svg" width={this.props.size[0]} height={this.props.size[1]}>
      {countries}
      <svg id="line-div"></svg>
    </svg>
  }
}

const appdata = worlddata.features
  .filter(d => geoCentroid(d)[0] < -20)

const nodes = [];
appdata
  .forEach((d,i) => {
    const offset = Math.random()
    d.launchday = i
    d.data = range(30).map((p,q) => q < i ? 0 : Math.random() * 2 + offset)

    var centroid = geoCentroid(d);
    if (centroid.some(isNaN)) return;
    centroid.x = centroid[0];
    centroid.y = centroid[1];
    centroid.feature = d;
    nodes.push(centroid);

  })


const colorScale = scaleThreshold().domain([5,10,20,30]).range(["#75739F", "#5EAFC6", "#41A368", "#93C464"])

class App extends Component {
  constructor(props){
    super(props)
    this.onResize = this.onResize.bind(this)
    this.onHover = this.onHover.bind(this)
    this.state = { screenWidth: 1000, screenHeight: 800, hover: "", brushExtent: [0,40], selected_nodes: [] }
    
  }
  onResize() {
    this.setState({ screenWidth: window.innerWidth, screenHeight: window.innerHeight - 120 })
  }
  onHover(d) {
    this.setState({ hover: d.id })
    const  selected_nodes = this.state.selected_nodes.slice()
    selected_nodes.push(d)
    this.setState({ selected_nodes: selected_nodes })
    var svg = document.getElementById('world-svg')
    console.log(svg)
    var centroid = geoCentroid(d);
    if (centroid.some(isNaN)) return;
    centroid.x = centroid[0];
    centroid.y = centroid[1];
    centroid.feature = d;



  }

  componentDidMount() {
    window.addEventListener('resize', this.onResize, false)
    this.onResize()
  }

  render() {
    const filteredAppdata = appdata
      .filter((d,i) => d.launchday >= this.state.brushExtent[0] && d.launchday <= this.state.brushExtent[1])
    return (
      <div className="App">
        <div className="App-header">
          <h2>d3ia dashboard</h2>
          <CountryLabel label={this.state.hover} />
        </div>
        <div className="row">
        <WorldMap hoverElement={this.state.hover} onHover={this.onHover} colorScale={colorScale} data={filteredAppdata} size={[this.state.screenWidth / 3, this.state.screenHeight ]} />
        <BarChart hoverElement={this.state.hover} onHover={this.onHover} colorScale={colorScale} data={filteredAppdata} size={[this.state.screenWidth / 3, this.state.screenHeight ]} />
        </div>
      </div>
    )
  }
}


export default App