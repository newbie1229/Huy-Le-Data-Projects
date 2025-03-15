import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # np.random.seed(123)
    all_walks = []
    # simulate random walks
    for i in range(500):
        random_walk = [0] #the result of each simulation 
        # roll the dice 100 times
        for j in range(100):
            step = random_walk[-1] # step starts at 0
            dice = np.random.randint(1,7)
            if dice <=2:
                step = max(0, step - 1)
                # can't go below 0
            elif dice<=5:
                step +=1
            else:
                step += np.random.randint(1,7)
            # falling down the stairs
            if np.random.rand() <= 0.001:
                step = 0
            random_walk.append(step)
        all_walks.append(random_walk)
        
    np_all_walks = np.transpose(np.array(all_walks))
    # visualize the random walks
    plt.plot(np_all_walks)
    plt.title('Random walks plot')
    plt.show()

    final_results = np_all_walks[-1,:]
    # Visualize the distribution of final_results
    plt.clf()
    plt.hist(final_results)
    plt.title('Final step of each simulation visualization')
    plt.show()
    
    c = 0
    for i in final_results:
        if i >= 60:
            c +=1
    print(f'The percent of winning the game is {c/500 * 100}%')

    
    