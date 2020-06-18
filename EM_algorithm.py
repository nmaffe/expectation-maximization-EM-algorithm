import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def likelihood(x, mu, sigma):
	return 1/(sigma * np.sqrt(2 * np.pi))*np.exp( - np.power((x - mu)/sigma, 2.0)/2. ) 

	
#print(likelihood(0, 0, 0.3))
#print(norm.pdf(0, 0, 0.3))

#x_values = np.linspace(-10, 10, 500)
#plt.plot(x_values, likelihood(x_values, 0.0, 1.0))
#plt.show()


np.random.seed(seed=1)
N = 1000

#Generate N numbers normally distributed with mean and sigma
mu_a, sigma_a = 0.0, 3.0 
n_a = np.random.normal(mu_a, sigma_a, N)
mu_b, sigma_b = 7.0, 1.0 
n_b = np.random.normal(mu_b, sigma_b, N)

nbins = 30
# Plots distributions. Note that density = True normalizes the distribution
count_a, bins_a, ignored_a = plt.hist(n_a, bins=nbins, density=True, color='salmon')#Plot distribution
count_b, bins_b, ignored_b = plt.hist(n_b, bins=nbins, density=True, color='lightskyblue')#Plot distribution


# This is the set of numbers drawn from the two normal distributions of which we want to estimate the parameters 
n = np.concatenate((n_a, n_b), axis=0)

# Set prior
pa, pb = 0.5, 0.5

# Set first guesses of parameters for the two gaussians
# Note that the starting guesses are crucial in the sense that
# mu_a should be lower than mu_b
guesses_mu_a, guesses_mu_b = [-7.0], [-6.0] 
guesses_sig_a, guesses_sig_b = [1.0], [1.0]

# This is for plotting the guessed distributions
x_values = np.linspace(-10, 11, 500)

# Expectation-Maximization (EM) algorithm
for it in range(20):

	# Set guesses for this iteration
	mu_a, mu_b = guesses_mu_a[-1], guesses_mu_b[-1]
	sig_a, sig_b = guesses_sig_a[-1], guesses_sig_b[-1]

	# Create arrays of poteriors. They will be used as weights
	posteriors_b = []
	posteriors_a = []
	
	# For each point x, calculate the posterior for p(a|x) and p(b|x) using Bayes theorem
	for i, x in enumerate(n):

		# Calculate the posterior probabilities of the point being from distr a or b
		bi = (likelihood(x, mu_b, sig_b) * pb) / (likelihood(x, mu_b, sig_b)*pb + likelihood(x, mu_a, sig_a)*pa)
		ai = 1 - bi

		#print(i, x, bi, ai)
		
		posteriors_b.append(bi)
		posteriors_a.append(ai)

	# Calculate new estimates for the parameters using the posteriors as weights in a weighted average
	
	new_mu_a = np.average(n, weights=posteriors_a)	
	new_mu_b = np.average(n, weights=posteriors_b)

	new_sig_a = np.average( (n-np.full_like(n, mu_a))**2, weights=posteriors_a)	
	new_sig_b = np.average( (n-np.full_like(n, mu_b))**2, weights=posteriors_b)
	new_sig_a = np.sqrt(new_sig_a)	
	new_sig_b = np.sqrt(new_sig_b)


	# Upload parameter lists with new parameters
	guesses_mu_a.append(new_mu_a)	
	guesses_mu_b.append(new_mu_b)
	guesses_sig_a.append(new_sig_a)
	guesses_sig_b.append(new_sig_b)

	print('%.2f %.2f' %(new_mu_a, new_mu_b))
	print('%.2f %.2f' %(new_sig_a, new_sig_b))

	print('Finished iteration', it)

	plt.plot(x_values, likelihood(x_values, guesses_mu_a[it], guesses_sig_a[it]), linewidth=2, color='peachpuff')
	plt.plot(x_values, likelihood(x_values, guesses_mu_b[it], guesses_sig_b[it]), linewidth=2, color='lightblue')

# Get best guesses
best_mu_a = guesses_mu_a[-1]
best_mu_b = guesses_mu_b[-1]
best_sig_a = guesses_sig_a[-1]
best_sig_b = guesses_sig_b[-1]

plt.plot(x_values, likelihood(x_values, best_mu_a, best_sig_a), linewidth=2, color='r')
plt.plot(x_values, likelihood(x_values, best_mu_b, best_sig_b), linewidth=2, color='b')


plt.show()



