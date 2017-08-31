import datetime
import hashlib as hasher


class StoryBlock:
    def __init__(self, writer, text, previous_index):
        self.timestamp = datetime.datetime.now()
        self.writer = writer
        self.text = text
        self.previous_index = previous_index
        self.index = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        to_be_hash = str(self.writer) + \
                     str(self.timestamp) + \
                     str(self.text) + \
                     str(self.previous_index)
        encoded_to_be_hash = to_be_hash.encode('utf-8')
        sha.update(encoded_to_be_hash)
        return sha.hexdigest()


def create_genesis_block():
    writer = "stereoF"
    text = "A long time ago in a galaxy far, far away"
    previous_index = "May the force be with you"
    return StoryBlock(writer, text, previous_index)


def next_block(last_block):
    writer = "FFF"
    previous_index = last_block.index
    text = "last block: " + previous_index
    return StoryBlock(writer, text, previous_index)


storychain = [create_genesis_block()]
previous_block = storychain[0]

num_of_blocks = 15

for i in range(0, num_of_blocks):
    new_block = next_block(previous_block)
    storychain.append(new_block)
    previous_block = new_block
    print("New block is: {}.".format(new_block.index))
    print("The text is: {}.".format(new_block.text))