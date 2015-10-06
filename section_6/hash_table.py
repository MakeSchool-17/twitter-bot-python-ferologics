class Hash_table(object):

    # needed primes in for of '4k + 3'
    primes = [78139, 147451, 290023, 367651, 466183, 590659, 958051, 1221751, 1561423, 1999891, 6919723, 11381863, 18722983, 39545731, 50796679, 65249803, 83546011, 107332723, 137421331, 176548243, 290395711, 479350519, 613693963, 788477863, 1013037943, 1300907011]

    def __init__(self):
        # or load factor, number of entries in the hash_table
        self.num_of_keys = 0
        # k defines the index of size in the primes array
        self.k = 0
        # size defined by kth index
        self.size = self.primes[self.k]  # always a prime
        # blank hash table with initial size
        self.hash_table = [None] * self.size

    # extend the existing hash_table by the difference between the new size and old_size
    def resize(self):
        old_size = self.size
        self.k += 1
        new_buckets = [None] * (self.size - old_size)
        self.hash_table.extend(new_buckets)

    def qhash(self, i, key):
        print(i)
        # use stock hash for first hash
        if i == 0:
            bucket_index = hash(key) % self.size
            print(bucket_index)
            # assign bucket's bucket index
        else:  # if conflict then hash with qhash
            # compute the bucket index
            if i % 2 == 0:  # if i is even +
                bucket_index = (hash(key) + pow(i, 2)) % self.size
            else:           # else -
                bucket_index = (hash(key) - pow(i, 2)) % self.size

        print(bucket_index)
        return bucket_index

    # assign new buckets to all bucketents in the hash_table after resize
    def rehash(self):
        # enumerate the hash_table
        for i, old_bucket in enumerate(self.hash_table):
            key, value = old_bucket

            # set the bucket index from qhash fucntion
            bucket_index = self.qhash(i, key)

            new_bucket = self.hash_table[bucket_index]

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
        for i in range(0, (self.size - 1)):

            bucket_index = self.qhash(i, key)

            # reassign the bucket's new bucket_index
            bucket = self.hash_table[bucket_index]
            print(bucket)
            # if bucket is None store the key and inc. num_of_keys
            if bucket is None:  # if bucket empty -> store
                self.hash_table[bucket_index] = (key, 1)
                self.num_of_keys += 1
                print('bucket was none')
                return
            # if bucket is already stored, just increment the value
            elif bucket[0] == key:  # if key is = to key in bucket ++
                old_tuple = self.hash_table[bucket_index]
                new_tuple = (old_tuple[0], (old_tuple[1] + 1))
                self.hash_table[bucket_index] = new_tuple
                return

    # get bucketent for a certain key in hash_table
    def get(self, key):

        for i in range(0, (self.size - 1)):

            if i == 0:  # primary hash, without qhashing
                # use stock hash for first hash
                bucket_index = hash(key) % self.size
                # assign bucket's bucket index
                bucket = self.hash_table[bucket_index]
            else:  # use qhash
                if i % 2 == 0:  # if i is even +
                    bucket_index = (hash(key) + (i * i)) % self.size
                else:           # else -
                    bucket_index = (hash(key) - (i * i)) % self.size
                # reassign the bucket to a different bucket
                bucket = self.hash_table[bucket_index]

            # if found -->
            if bucket[0] == key:
                print("Found key '" + str(bucket[0]) + "' with value '" + str(bucket[1]) + "'")
                return bucket
        # if not found -->
        print("Key " + key + " was not found T_T")
        return None

    # hash_table all the keys in all the buckets in the tuples
    def keys(self):
        keys = []
        for bucket in enumerate(self.hash_table):
            if bucket[1] is not None:
                keys.append(bucket[1][0])
        return keys

    # hash_table all the values in all the buckets in the tuples
    def values(self):
        values = []
        for bucket in enumerate(self.hash_table):
            if bucket[1] is not None:
                values.append(bucket[1][1])
        return values

    # used to update a certain value in a bucket in a linked hash_table
    def update(self, key, value):
        self.get(key)[1] = value

if __name__ == "__main__":
    hash_t = Hash_table()

    hash_t.insert("meh")
    hash_t.insert("meh")
    hash_t.insert("meh")

    hash_t.insert("huehue")
    hash_t.insert("huehue")
    hash_t.insert("huehue")

    hash_t.get("meh")
    hash_t.get("huehue")

    print(hash_t.keys())
    print(hash_t.values())
