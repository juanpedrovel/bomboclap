# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_times = Queue(size)
        self.busy_until = 0

    def Process(self, request):
        a = request.arrival_time
        p = request.process_time
        f = max(self.busy_until, a) + p
        self.size = self.finish_times.dequeue(a)
        self.size = self.finish_times.enqueue(f)
        if self.size == None:
            return Response(True, -1)
        self.busy_until = f
        return Response(False, self.busy_until - p)

class Queue:
    def __init__(self, size):
        self.elements = [0] * (size)
        self.head = 0
        self.tail = 0
        self.size = size
        self.available_size = size

    def enqueue(self, element):
        if self.available_size > 0:
            self.elements[self.tail] = element
            self.tail = (self.tail + 1) % self.size
            self.available_size -= 1
            return self.available_size
        else:
            return None

    def dequeue(self, element):
        while self.elements[self.head] <= element and self.available_size < self.size:
            self.head = (self.head + 1) % self.size
            self.available_size += 1
        return self.available_size

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
