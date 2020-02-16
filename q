[1mdiff --git a/sampleapp/static/style/style.css b/sampleapp/static/style/style.css[m
[1mindex 3b9c7e4..3c72b41 100644[m
[1m--- a/sampleapp/static/style/style.css[m
[1m+++ b/sampleapp/static/style/style.css[m
[36m@@ -163,6 +163,8 @@[m [ma {[m
 [m
 .mosaic_image{[m
   width: 90%;[m
[32m+[m[32m  min-height: 200px;[m
[32m+[m[32m  max-height: 200px;[m
   overflow: hidden;[m
   z-index: 1;[m
   transition: transform .2s;[m
[1mdiff --git a/sampleapp/templates/project_detail.html b/sampleapp/templates/project_detail.html[m
[1mindex 670e75b..38830d0 100644[m
[1m--- a/sampleapp/templates/project_detail.html[m
[1m+++ b/sampleapp/templates/project_detail.html[m
[36m@@ -22,7 +22,11 @@[m
 	    		%}/>[m
 	    	</div>[m
 	    	{% endif %}[m
[31m-[m
[32m+[m	[41m    [m	[32m  <div style="font-family: courier, monospace; margin-left: 100px; margin-right: 100px; margin-top: 50px; margin-bottom: 50px; justify-content: left;" align="left">[m
[32m+[m[41m    [m				[32m<font size="4" >[m
[32m+[m	[41m    [m				[32m<p> {{project.content }}</p>[m
[32m+[m	[41m    [m			[32m</font>[m
[32m+[m	[41m    [m		[32m</div>[m
 	[m
 		{% endblock %}[m
 {% endblock %}[m
