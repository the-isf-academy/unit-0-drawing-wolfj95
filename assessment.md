# Assessment

When your project is finished (or before if it's helpful), assess your project. Read the [project rubric](http://cs.fablearn.org/projects/0-drawing project.html) and then decide how your project should score on each category. Write a paragraph for each category justifying this assessment with evidence from your code, planning documents, and commit messages.

## [A] Knowing, understanding, and computational thinking
### [A.iii] Controlling the flow of a program
**My project achieves level 8 expectations on this category. Here's why.**
I spent a lot of time thinking about how to make the bottle rotate around the x-axis so that both the ovals and the cylinder portion of the bottle seemed 3 dimensional from all angles.

I used loops throughout my program but one that I'm particularly proud of is the loop in my draw_taper() function which simultaneously loops through the points on a smaller oval and larger oval and maps points on the larger oval to points on the smaller oval. To do this, I had to loop through the points at different rates (since there are more points on the larger oval) which was a fun challenge to figure out.

You can also see where I reorganized my code in my commit titled "Created taper" because I decided to use the restore_state_when_finished context manager instead of trying to reposition the turtle after a function on my own. This allowed me to cut out some unnecessary lines of code.

### [A.iv] Decomposition and abstraction
**My achieves level project 7 expectations on this category. Here's why.**
I think my project is well decomposed into smaller chunks. The big problem of drawing the bottle is broken down into drawing the base and the cap and these functions are broken down into smaller parts like draw_oval() and draw_cylinder(). The smallest level functions are generalized so that I could use them for each part of the project (which turned out to be a lot of ovals and cylinders)

My project only achieves a 7 (and not an 8) because I some of my functions are still not very well abstracted. Specifically, I draw the outlines of the cylinders (in grey) for every cylinder but this doesn't really make sense in my drawing. I could have draw the outlines separately or used an optional argument to tell my functions to draw the outlines.

## [B] Planning and development

## [B.i] The proposal
**My project achieves level 7 expectations on this category. Here's why.**
I have commented each of my functions with the expected inputs and outputs of the function as well as a description of what the function does. MY planning document offers an overview of the project and what's included in each file, with a description of each function.

## [B.ii] Plans, milestones, and timelines
**My project achieves level 7 expectations on this category. Here's why.**
My project proposal was helpful to me when planning out my work. It helped me prioritize my work by helping me realize that I needed to start by figuring out how to draw an oval and thne a cylinder from there. Initially, I did not anticipate correctly the amount of time the more basic parts of my project would take (like drawing an oval and a cylinder) but having the plan allowed me to make up for lost time after the basic parts of my project were completed.

## [B.iii] Documentation
**My project achieves level 4 expectations on this category. Here's why.**
The development of my project is pretty poorly documented. I did not make very many commits and there were huge changes between each of my commits. This made describing the work I did very difficult, and so my commit messages are not very descriptive. Still, I have some commit messages and you can get an idea of the work I did to complete this project.

## [B.iv] Personally meaningful project
**My project achieves level 6 expectations on this category. Here's why.**
I think this project was meaningful to me because I chose a meaningful object and also chose a challenge that was appropriate to my level of experience. Still, it wasn't the most creative project I've ever done, and I wish I would have incorporated earlier more ways for the project to express more parts of myself.
