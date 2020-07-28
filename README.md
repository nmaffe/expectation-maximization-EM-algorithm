# Expectation-Maximization (EM) algorithm
## 1-dimensional simple case


What's the objective: given two populations of numbers drawn from 2 gaussian distributions, estimate the 2 gaussian parameters (means and the variances).  

Let's see how this works.

Suppose our experimental setup registers numbers from 2 gaussian sources, let's call them red and blue. 
Then we have then 2 sets of numbers distributed according to two 1D gaussian distributions (in the exercise case we have generated them synthetically).  

If we knew which numbers belongs to which distribution, we could easily estimate the means and the variances of the two distributions by calculating:

![eq1](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5Cmu_b%20%3D%20%5Cfrac%7Bx_1%20&plus;%20x_2%20&plus;%20...%20&plus;%20x_%7Bn_b%7D%7D%7Bn_b%7D)

![eq2](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5Csigma%5E2_b%20%3D%20%5Cfrac%7B%28x_1-%5Cmu_b%29%5E2%20&plus;%20%28x_2-%5Cmu_b%29%5E2%20&plus;%20...%20&plus;%20%28x_%7Bn_b%7D-%5Cmu_b%29%5E2%7D%7Bn_b%7D)

for the set (x_1, x_2, ..., x_nb) of the blue distribution and similarly for the red distribution. Then we are happy and completed the task. 

But let's say we don't know which numbers belong to which distribution. Then the problem looks challenging. However, let's assume we have an initial guess of the distribution parameters (means and variances). Then for each point x_i in our dataset we could calculate the probability b_i of that point belonging to the blue (Px_i|b) distribution, by using the Bayes Theorem:

![eq3](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20b_i%20%3D%20P%28b%7Cx_i%29%20%3D%20%5Cfrac%7BP%28x_i%7Cb%29P%28b%29%7D%7BP%28x_i%7Cb%29P%28b%29&plus;P%28x_i%7Cr%29P%28r%29%7D)

![eq4](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20P%28x_i%7Cb%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi%20%5Csigma_b%7D%7De%5E%7B-%5Cfrac%7B%28x-%5Cmu_b%29%5E2%7D%7B2%5Csigma_b%5E2%7D%7D)

and similarly for red. We have also assumed some value for the prior P(b) and P(r). As mentioned above, the distribution parameters (means and variances) we use in the likelihood P(x_i|b) and P(x_i|r) are our initial guesses. 
Each point x_i is therefore associated with a probability b_i and r_i to belong to the blue distribution and to the red distribution. This is a 'soft clustering' technique since each point it's given some probability to belong to both distributions (unlike K-mean clustering, which is a 'hard clustering' technique). 

The next step is to re-estimate the means (and the variances) of the two distributions given the b_i's and the r_i's we have just calculated. We use them as weights in a weighted mean. For example, the new estimates of the blue parameters are:

![eq5](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5Cmu_b%20%3D%20%5Cfrac%7Bx_1b_1%20&plus;%20x_2b_2%20&plus;%20...%20&plus;%20x_nb_n%7D%7Bb1%20&plus;%20b2%20&plus;%20...%20&plus;%20b_n%7D)

![eq6](https://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20%5Csigma%5E2_b%20%3D%20%5Cfrac%7Bb_1%28x_1-%5Cmu_b%29%5E2%20&plus;%20b_2%28x_2-%5Cmu_b%29%5E2%20&plus;%20...%20&plus;%20b_n%28x_n-%5Cmu_b%29%5E2%7D%7Bb_1%20&plus;%20b_2%20&plus;%20...%20&plus;%20b_n%7D)

and similarly for the red parameters. 
The procedure can be iterated again by calculating at each step the new b_i's and r_i's using the parameters of the previous iteration and estimating the new parameters. Eventually, after some iterations the new parameters will converge to some final values. These will be our final estimates of the distribution paramters. 

