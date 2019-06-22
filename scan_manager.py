import subprocess

class ScanManager():

    def __init__(self, data):
        self.__id = None
        self.current_process = None
        self.data = data

    def set_id(self, id):
        self.__id = id
        return True
    
    def get_id(self):
        return self.__id
    
    def _start_process(self, id):
        args = ['say', self.data[id]['text']]
        self.current_process = subprocess.Popen(args)

    def process_id(self,new_id):
        #create a thread to run sound pulled from file
        #check current thread to verify it has completed

        #if it's a new id
        if new_id != self.__id: #will also want to add some sort of count validator here #ToDo
            if self.current_process is None:
                # no process created yet, start one and set id
                self._start_process(new_id)
                self.__id = new_id
            else: # a process has already been created, lets check it
                #if process is still running, don't do anything
                if self.current_process.poll() == 0: #last process is done
                    #Need to generate args and pass to the mp3 player
                    self._start_process(new_id)
                    self.__id = new_id
        else: #not a new id, is the process done, now play with counts
            if self.current_process.poll() == 0: #last process is done
                #Need to generate args and pass to the mp3 player
                self._start_process(new_id)



        



