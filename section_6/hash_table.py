class Hash_table(object):

    def __init__(self):
        # needed primes in for of '4k + 3'
        self.primes = [78139, 147451, 290023, 367651, 466183, 590659, 958051, 1221751, 1561423, 1999891, 6919723, 11381863, 18722983, 39545731, 50796679, 65249803, 83546011, 107332723, 137421331, 176548243, 290395711, 479350519, 613693963, 788477863, 1013037943, 1300907011]
        # or load factor, number of entries in the hash_table
        self.num_of_keys = 0
        # k defines the index of size in the primes array
        self.k = 0
        # size defined by kth index
        self.size = self.primes[self.k]  # always a prime
        # blank hash table with initial size
        self.hash_table = [[None]] * self.size

    # extend the existing hash_table by the difference between the new size and old_size
    def resize(self):
        old_size = self.size
        self.k += 1
        new_buckets = [[None]] * (self.size - old_size)
        self.hash_table.extend(new_buckets)

    # assign new buckets to all elements in the hash_table after resize
    def rehash(self):
        # enumerate the hash_table
        for i, old_bucket in enumerate(self.hash_table):
            key, value = old_bucket

            if i % 2 == 0:  # if i is even +
                elem_index = (hash(key) + (i * i)) % self.size
            else:           # else -
                elem_index = (hash(key) - (i * i)) % self.size

            new_bucket = self.hash_table[elem_index]

            if new_bucket is None:
                new_bucket = (key, 1)
                self.num_of_keys += 1

            elif new_bucket[0] == key:  # if key is = to key in bucket
                new_bucket[1] += 1

    # test load factor and decide if should resize
    def should_resize(self):
        if self.load_factor() >= .66666666666:
            return True
        return False

    # check how filled the hash table is
    def load_factor(self):
        return (self.num_of_keys / self.size)

    # insert (store) value for a new key
    def insert(self, key):
        # resize if needed
        if self.should_resize():
            self.resize()
            self.rehash()

        # store
        for i in range(self.size):

            # use stock hash for first hash
            if i == 0:
                bucket_index = hash(key) % self.size
                # assign elem's bucket index
                elem = self.hash_table[bucket_index]
            else:  # if conflict then hash with qhash
                # compute the bucket index
                if i % 2 == 0:  # if i is even +
                    bucket_index = (hash(key) + (i * i)) % self.size
                else:           # else -
                    bucket_index = (hash(key) - (i * i)) % self.size

                # reassign the elem's new bucket_index
                elem = self.hash_table[bucket_index]

            # if elem is None store the key and inc. num_of_keys
            if elem is None:  # if bucket empty -> store
                elem = (key, 1)
                self.num_of_keys += 1
                break
            # if elem is already stored, just increment the value
            elif elem[0] == key:  # if key is = to key in bucket ++
                elem[1] += 1
                break

    # get element for a certain key in hash_table
    def get(self, key):

        for i in range(self.size):

            if i == 0:  # primary hash, without qhashing
                # use stock hash for first hash
                bucket_index = hash(key) % self.size
                # assign elem's bucket index
                elem = self.hash_table[bucket_index]
            else:  # use qhash
                if i % 2 == 0:  # if i is even +
                    bucket_index = (hash(key) + (i * i)) % self.size
                else:           # else -
                    bucket_index = (hash(key) - (i * i)) % self.size
                # reassign the elem to a different bucket
                elem = self.hash_table[bucket_index]

            # if found -->
            if elem[0] == key:
                print("Found key '" + elem[0] + "' with value '" + elem[1] + "'")
                return elem
        # if not found -->
        print("Key " + key + " was not found T_T")
        return None

    # hash_table all the keys in all the buckets in the tuples
    def keys(self):
        keys = None
        for bucket in enumerate(self.hash_table):
            keys.append(bucket[0])

    # hash_table all the values in all the buckets in the tuples
    def values(self):
        values = None
        for bucket in enumerate(self.hash_table):
            values.append(bucket[0])

    # used to update a certain value in a bucket in a linked hash_table
    def update(self, key, value):
        self.get(key)[1] = value
