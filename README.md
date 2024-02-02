# IVul-Image-based vulnerability detection under backdoor attack
Lorena González-Manzano and Joaquin Garcia-Alfaro 

(Universiad Carlos III de Madrid/ SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris, Palaiseau, 91120, France)
#

This repository contains used data (namely computed code metrics and tokens) and complete results of the paper "Image-based vulnerability detection under backdoor attack. Lorena González-Manzano and Joaquin Garcia-Alfaro (submitted for evaluation)".

Files are the following:

-There are 2 .xlsx files (resultsGitHubCSHARP/ resultsGitHubPHP) which contain baseline results of the use of IVul and results per proposed threat model after executed attacks. 

-There are 2 folders (PHP/CSHARP baseline) containing generated images per each programming language used in baseline computations

-There are 2 folders (PHP/CSHARP attacks) containing generated images per each programming language used in attacks computations

-'Code_image_generation_GitHub.py' is the general script used to generate images from code samples.

-php/csharpSamples.csv contain code samples. In particular, per code samples the following information is provided: identifier, state that is bad(vulnerable) or good (no vulnerable), submissionDateYear,submissionDateMonth,submissionDay, CWE and code

