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
        print("=========================RESIZING==========================")
        # store the old size
        old_size = self.size
        # print("Old size --> " + str(old_size))
        # increase the index of the current size in the primes list
        self.k += 1
        # print("k --> " + str(self.k))
        # set new size
        self.size = self.primes[self.k]
        # print("New size --> " + str(self.size))
        # initialize new buckets to match the new size
        new_buckets = [None] * (self.size - old_size)
        # print("New buckets --> " + str(new_buckets))
        # extent Htable by the number of buckets needed to mach the prime size
        self.hash_table.extend(new_buckets)
        # print("Resized hash table --> " + str(self.hash_table))

    # reassign buckets in the hash_table after resize
    def rehash(self):
        print("=========================REHASHING=========================")
        # enumerate the hash_table
        new_hash_table = [None] * self.size
        for old_bucket in enumerate(self.hash_table):
            # if the bucket has a value (a tuple) rehash and store it
            if old_bucket[1] is not None:
                # print("r: Start: old bucket --> " + str(old_bucket[1]))
                # set the new bucket index from qhash fuc(passing in the key)
                new_bucket_index = self.qhash(old_bucket[1][0])
                # print("r: new bucket index --> " + str(new_bucket_index))
                # assign new bucket for new size
                new_hash_table[new_bucket_index] = old_bucket[1]
                # print("r: rebased --> " + str(new_hash_table[new_bucket_index]))
        self.hash_table = new_hash_table

    """quadratic probing modification first suggested by C. Radke in the article "The use of quadratic residue research" (1970), which allows to probe all slots in the hash table exactly once, i. e. the probing sequence is a permutation of the slots."""
    # return the bucket_index of certain key
    def qhash(self, key):
        # to avoid extensive if statements later when Qhashing
        operator = -1
        print("=========================QHASHING==========================")
        for i in range(0, self.size - 1):
            # print("q: --> Hash attempt #" + str(i))
            # changing operator to + or - every loopthrough
            operator *= -1
            # print("q: --> Hash operator --> " + str(operator))
            # compute the bucket index
            bucket_index = (hash(key) + (pow(i, 2) * operator)) % self.size
            # print("q: --> Hash bucket index --> " + str(bucket_index))
            # if it's 0 it doesn't add anything so it's a stock hash :)
            if self.hash_table[bucket_index] is None or str(self.hash_table[bucket_index][0]) == key:
                # print("q: --> The returning bucket index is #" + str(bucket_index))
                return bucket_index

    # test load factor and decide if should resize
    def should_resize(self):
        # if the load factor is more than aprox 2/3 return True
        if self.load_factor() >= .66666666666:
            # print(" --> Returned True")
            return True
        # print(" --> Returned False")
        return False

    # check how filled the hash table is
    def load_factor(self):
        # print("Load factor --> " + str(self.num_of_keys / self.size))
        return (self.num_of_keys / self.size)

    # insert (store) value for a new key
    def insert(self, key):
        """ TODO: document non-standard insert behavior on redundant key
        """
        print("=========================INSERTING=========================")
        # resize if needed
        if self.should_resize():
            # print("i: 'should_resize' evaluated to True")
            self.resize()
            self.rehash()

        # assign the bucket index from qhash
        bucket_index = self.qhash(key)
        # print("i: Insert index --> " + str(bucket_index))
        # reassign the bucket's new bucket_index
        bucket = self.hash_table[bucket_index]
        # print("i: Insert bucket --> " + str(bucket))
        # if bucket is None store the key and increment num_of_keys
        if bucket is None:
            self.hash_table[bucket_index] = (key, 1)
            print("i: Stored key to empty bucket --> " + str(self.hash_table[bucket_index]))
            self.num_of_keys += 1

        # if bucket is already stored, just increment the value
        elif bucket[0] == key:
            old_key, old_value = self.hash_table[bucket_index]
            new_tuple = (old_key, old_value + 1)
            self.hash_table[bucket_index] = new_tuple
            print("i: Incremented value associated with key --> " + str(new_tuple))

    # get index and bucket for a key in form of tuple (index, bucket)
    def get(self, key):
        print("==========================GETTING==========================")
        i = 0
        while i < self.size:
            # qhash - hash and add the i to the power of 2, % for bucket index
            index = (hash(key) + pow(i, 2)) % self.size
            # print("g: Some bucket index --> " + str(index))
            bucket = self.hash_table[index]
            # print("g: Some bucket --> " + str(bucket))
            # use stock hash for first hash      AND
            # if the buckets key is equal to key we're searching for
            if bucket is not None and bucket[0] == key:
                print("g: --> Found key '" + str(bucket[0]) + "' with value '" + str(bucket[1]) + "'")
                # return the tuple stored in bucket
                return (index, bucket)
            i += 1
        print("g: --> Key " + key + " was not found T_T")
        return None

    # hash_table all the keys in all the buckets in the tuples
    def keys(self):
        # init blank array
        keys = []
        for bucket in enumerate(self.hash_table):
            if bucket[1] is not None:
                keys.append(bucket[1][0])
        return keys

    # hash_table all the values in all the buckets in the tuples
    def values(self):
        # init blank array
        values = []
        for bucket in enumerate(self.hash_table):
            if bucket[1] is not None:
                values.append(bucket[1][1])
        return values

    # update a certain value in a bucket in the hash table
    def update(self, key, new_value):
        # store bucket from get(key) fucntion
        bucket = self.get(key)
        # get the index
        index_of_bucket = bucket[0]
        # test for None value
        if bucket[1] is not None:
            self.hash_table[index_of_bucket][1] = new_value


def main():
    hash_t = Hash_table()

    hash_t.insert("meh")
    hash_t.get("meh")

    hash_t.resize()
    hash_t.rehash()

    hash_t.insert("meh")

    hash_t.get("meh")

    print()
    #
    # print(hash_t.keys())
    # print(hash_t.values())
    #
    #
    # hash_t.insert("meh")
    #
    # hash_t.get("meh")
    #
    # print(hash_t.keys())
    # print(hash_t.values())

if __name__ == "__main__":
    main()
