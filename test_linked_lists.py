import unittest

from linked_lists import SinglyLinkedList, DoublyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = [(2, 4), (4, 6), (6, 5), (5, None)]
        self.r_list = [(5, 6), (6, 4), (4, 2), (2, None)]
        self.head = self.list[0]
        self.r_head = self.r_list[0]

        self.append_data = 9
        self.append_list = [(2, 4), (4, 6), (6, 5), (5, self.append_data),
                            (self.append_data, None)]
        self.append_r_list = [(5, 6), (6, 4), (4, 2), (2, self.append_data),
                              (self.append_data, None)]

        self.prepend_data = 0
        self.prepend_list = [(self.prepend_data, 2), (2, 4), (4, 6), (6, 5),
                             (5, None)]
        self.prepend_r_list = [(self.prepend_data, 5), (5, 6), (6, 4), (4, 2),
                               (2, None)]

        self.insert_data = (8, 2)
        self.insert_list = [(2, 4), (4, self.insert_data[0]),
                             (self.insert_data[0], 6), (6, 5), (5, None)]
        self.insert_r_list = [(5, 6), (6, self.insert_data[0]),
                              (self.insert_data[0], 4), (4, 2), (2, None)]

        self.del_data = 4
        self.del_list = [(2, 6), (6, 5), (5, None)]
        self.del_r_list = [(5, 6), (6, 2), (2, None)]

    def create_list(self, reverse=False):
        lst = SinglyLinkedList()
        for data, next in self.list:
            lst.append(data)
        if reverse:
            lst.reverse()
        return lst

    @staticmethod
    def repr_list(lst):
        current = lst.head
        repr_list = []
        while current:
            if current.next_:
                repr_list.append((current.data, current.next_.data))
            else:
                repr_list.append((current.data, None))
            current = current.next_
        return repr_list

    def test_links(self):
        lst = self.create_list()
        current = lst.head
        self.assertEqual(self.head[0], current.data,
                         f"Reverse list head data must be {self.head[0]}")
        self.assertEqual(self.head[1], current.next_.data,
                         f"Reverse list head.next_ "
                         f"data must be {self.head[1]}")
        self.assertEqual(self.repr_list(lst), self.list)

    def test_reverse(self):
        rev_lst = self.create_list(reverse=True)
        current = rev_lst.head
        self.assertEqual(self.r_head[0], current.data,
                         f"Reverse list head data must "
                         f"be {self.r_head[0]}")
        self.assertEqual(self.r_head[1], current.next_.data,
                         f"Reverse list head.next_ data must "
                         f"be {self.r_head[1]}")
        self.assertEqual(self.repr_list(rev_lst), self.r_list)

    def test_append(self):
        lst = self.create_list()
        lst.append(self.append_data)
        self.assertEqual(self.repr_list(lst), self.append_list)

        rev_lst = self.create_list(reverse=True)
        rev_lst.append(self.append_data)
        self.assertEqual(self.repr_list(rev_lst), self.append_r_list)

    def test_prepend(self):
        lst = self.create_list()
        lst.prepend(self.prepend_data)
        self.assertEqual(self.repr_list(lst), self.prepend_list)

        rev_lst = self.create_list(reverse=True)
        rev_lst.prepend(self.prepend_data)
        self.assertEqual(self.repr_list(rev_lst), self.prepend_r_list)

    def test_insert(self):
        lst = self.create_list()
        lst.insert(*self.insert_data)
        self.assertEqual(self.repr_list(lst), self.insert_list)

        rev_lst = self.create_list(reverse=True)
        rev_lst.insert(*self.insert_data)
        self.assertEqual(self.repr_list(rev_lst), self.insert_r_list)

    def test_delete(self):
        lst = self.create_list()
        lst.delete(self.del_data)
        self.assertEqual(self.repr_list(lst), self.del_list)

        rev_lst = self.create_list(reverse=True)
        rev_lst.delete(self.del_data)
        self.assertEqual(self.repr_list(rev_lst), self.del_r_list)


if __name__ == '__main__':
    unittest.main()
