# Software Vulnerability Detection under Poisoning Attacks using CNN-based Image Processing
Lorena González-Manzano and Joaquin Garcia-Alfaro 

(Universidad Carlos III de Madrid / SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris, Palaiseau, 91120, France)
#

This repository contains used data (namely computed code metrics and tokens) and complete results of the paper "Image-based vulnerability detection under backdoor attack. Lorena González-Manzano and Joaquin Garcia-Alfaro (submitted for evaluation)".

Files are the following, though in some cases the compress version is provided due to size limitation:

-There are 2 .xlsx files (resultsGitHubCSHARP/ resultsGitHubPHP) which contain baseline results of the use of IVul and results per proposed threat model after executed attacks. 

-There are 2 folders (PHP/CSHARP baseline) containing generated images per each programming language used in baseline computations

-There are 2 folders (PHP/CSHARP attacks) containing generated images per each programming language used in attacks computations. Folders within these contain subfolders with the following pattern name: Poison<attack>[<%spaces 100=full and none=20>]<%poison>. For instance, PoisonDI10

In previous 4 folders, there are subfolders refering to the 3 sets of testing and training files generated (read paper for details) and each image is named as follows: CodeID<CWE>[<Poi if poisoned>]<state bad(vulnerable)/good(no vulnerable)>[<%poison 1=10, 2=25, 4=40> ]

-'Code_image_generation_GitHub.py' is the general script used to generate images from code samples.

-php/csharpSamples.csv contain code samples. In particular, per code samples the following information is provided: identifier, state that is bad(vulnerable) or good (no vulnerable), submissionDateYear,submissionDateMonth,submissionDay, CWE and code

