# python3

class Worker:
    def __init__(self, i):
        self.id = i
        self.busy_until = 0

class JobQueue:
    def read_data(self):
        self.num_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.workers = []
        self.start_times = []
        self.assigned_workers = []
        for i in range(self.num_workers):
            self.workers.append(Worker(i))
        assert self.m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        for j in range(self.m):      
            self.start_times.append(self.workers[0].busy_until)
            self.assigned_workers.append(self.workers[0].id)
            self.workers[0].busy_until += self.jobs[j]
            self.Swift_Down(0)

    def Swift_Down(self, i):
        min_index = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        if left_child < self.num_workers and self.workers[left_child].busy_until <= self.workers[i].busy_until:
            if self.workers[left_child].busy_until < self.workers[min_index].busy_until: 
                min_index = left_child
            else:
                if self.workers[left_child].id < self.workers[min_index].id:
                    min_index = left_child 
        if right_child < self.num_workers and self.workers[right_child].busy_until <= self.workers[min_index].busy_until:
            if self.workers[right_child].busy_until < self.workers[min_index].busy_until: 
                min_index = right_child
            else:
                if self.workers[right_child].id < self.workers[min_index].id:
                    min_index = right_child

        if i != min_index:
            self.workers[i], self.workers[min_index] = self.workers[min_index], self.workers[i]
            self.Swift_Down(min_index)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()
    


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

