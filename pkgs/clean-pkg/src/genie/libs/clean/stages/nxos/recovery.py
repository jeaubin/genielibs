'''NXOS specific recovery functions'''

# Python
import time


# Power Cycler handlers
def sendbrk_handler(spawn, break_count):
    ''' Send break while rebooting device
        Args:
            spawn ('obj'): Spawn connection object
            break_count ('int'): Number of sending break times
        Returns:
            None
    '''

    for _ in range(1, break_count):
        spawn.sendline("\003")
        time.sleep(.002)
