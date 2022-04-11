from lib.chinese_word_segmentation import segmentation
if __name__ == '__main__':
    # s = "python难不难，c++好简单。"
    # result = segmentation(s,with_sg=True)
    # print(result)
    from queue import PriorityQueue

    q = PriorityQueue()

    q.put(1)
    q.put(3)
    q.put(2)
    sorted(q,)
    while not q.empty():
        next_item = q.get()
        print(next_item)