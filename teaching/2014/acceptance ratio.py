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
    return n_accepted


n_runs = 500
n_trials = 1000
delta = 0
x=0
n_delta_list = []
sigmas = []

for m in range(1,50):
    delta=delta+0.1
    avg = 0.0
    n_delta_list.append(delta)
    for run in range(n_runs):
        ratio= markov_pi(n_trials, delta) / float(n_trials)
        avg += (ratio / n_runs)
    sigmas.append(avg)
    print delta,avg

pylab.plot(n_delta_list, sigmas, 'o')
pylab.xlabel('delta')
pylab.ylabel('acceptance ratio')
pylab.title('Acceptance ratio as a function of delta')
pylab.savefig('accept_ratio.pdf')
pylab.show()

