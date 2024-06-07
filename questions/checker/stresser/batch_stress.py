import stress_single
import threading

N = 4   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=stress_single.stress_test_singular, args=["127.0.0.1", 2, True])
    t.start()
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')