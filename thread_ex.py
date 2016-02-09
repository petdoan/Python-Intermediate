from threading import Thread

class InputReader(Thread):
    """Thread example, extends Thread class"""
    
    def run(self):
        """
        Whatever is in the run method (or called from
        it, is executed in a separate thread
        """
        self.line_of_text = input('Enter some text: ')

input('Are you ready? When you hit return the thread will start.')
thread = InputReader()
thread.start()

count, result = 1, 1

while thread.is_alive():
    result = count * count
    count += 1

print('calculated squares up to {0} * {0} = {1}'.format(count, result))
print('while you typed "{}"'.format(thread.line_of_text))

