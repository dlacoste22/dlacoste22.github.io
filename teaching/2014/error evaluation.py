import random, math, pylab

def markov_pi(N, delta):
    x, y = 1.0, 1.0
    n_hits = 0
    n_accepted = 0
    for i in range(N):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
            n_accepted +=1
        if x**2 + y**2 < 1.0: n_hits += 1
    return n_hits

n_delta=50
n_runs = 500
n_trials=1000
delta=0
sigmas = []
n_delta_list = []

for run in range(n_delta):
    delta = delta + 0.1
    sigma = 0.0
    for run in range(n_runs):
        pi_est = 4.0 * markov_pi(n_trials,delta) / float(n_trials)
        sigma += (pi_est - math.pi) ** 2
    #        print delta,run,math.sqrt(sigma/ float(n_runs))
    sigmas.append(math.sqrt(sigma/float(n_runs)))
    n_delta_list.append(delta)

pylab.plot(n_delta_list, sigmas, 'o')
pylab.xlabel('delta')
pylab.ylabel('$\sigma$')
pylab.title('Standard deviation $\sigma$ as a function of delta')
pylab.savefig('one-half-rule.pdf')
pylab.show()