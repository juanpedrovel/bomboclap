# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class Element:
    def __init__(self, element):
        self.element = element
        self.next = None


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [None] * bucket_count

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if chain:
            print(' '.join(chain))
        else:
            print('')

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            chain = []
            x = self.elems[query.ind]
            while x != None:
                chain.append(x.element)
                x = x.next
            self.write_chain(chain)
        else:
            if query.type == 'find':
                e = query.s
                h_pos = self._hash_func(e)
                if self.elems[h_pos] == None:
                    return self.write_search_result(False)
                else:
                    x = self.elems[h_pos]
                    while x != None:
                        if x.element == e:
                            return self.write_search_result(True)
                        x = x.next
                    return self.write_search_result(False)
               
            elif query.type == 'add':
                e = Element(query.s)
                h_pos = self._hash_func(e.element)
                if self.elems[h_pos] == None:
                    self.elems[h_pos] = e
                else:
                    x = self.elems[h_pos]
                    while x != None:
                        if x.element == e.element:
                            return
                        else:
                            x = x.next
                    e.next = self.elems[h_pos]
                    self.elems[h_pos] = e
            else:
                e = query.s
                h_pos = self._hash_func(e)
                if self.elems[h_pos] == None:
                    return
                else:
                    x = self.elems[h_pos]
                    y = x.next
                    if x.element != e:
                        while y != None:
                            if y.element == e:
                                x.next = y.next
                                y = None
                                break
                            x = y
                            y = y.next
                    elif y != None:
                        self.elems[h_pos] = y
                        x = None
                    else:
                        self.elems[h_pos] = None

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
