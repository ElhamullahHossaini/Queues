import tkinter as tk
#Priority Queue

class PriorityQueueGUI:
    def __init__(self):
        self.queue = []

        self.root = tk.Tk()
        self.root.title("Priority Queue GUI")
        self.root.geometry("400x300")

        # Input Label and Entry
        self.input_label = tk.Label(self.root, text="Enter item:")
        self.input_label.grid(row=0, column=0, sticky=tk.W)

        self.input_entry = tk.Entry(self.root)
        self.input_entry.grid(row=0, column=1, padx=10, pady=5)

        # Priority Label and Entry
        self.priority_label = tk.Label(self.root, text="Enter priority:")
        self.priority_label.grid(row=1, column=0, sticky=tk.W)

        self.priority_entry = tk.Entry(self.root)
        self.priority_entry.grid(row=1, column=1, padx=10, pady=5)

        # Enqueue Button
        self.enqueue_button = tk.Button(self.root, text="Enqueue", command=self.enqueue_item)
        self.enqueue_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Dequeue Button
        self.dequeue_button = tk.Button(self.root, text="Dequeue", command=self.dequeue_item)
        self.dequeue_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Peek Button
        self.peek_button = tk.Button(self.root, text="Peek", command=self.peek_item)
        self.peek_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Size Button
        self.size_button = tk.Button(self.root, text="Size", command=self.get_size)
        self.size_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Traverse Button
        self.traverse_button = tk.Button(self.root, text="Traverse", command=self.traverse_queue)
        self.traverse_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # Message Label
        self.message_label = tk.Label(self.root, text="", fg="red")
        self.message_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.root.mainloop()

    def enqueue_item(self):
        item = self.input_entry.get()
        priority = int(self.priority_entry.get())

        self.queue.append((item, priority))

        self.message_label.config(text=f"Item '{item}' with priority {priority} has been enqueued.")

        self.input_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def dequeue_item(self):
        if len(self.queue) == 0:
            self.message_label.config(text="Queue is empty.")
        else:
            highest_priority_item = max(self.queue, key=lambda x: x[1])
            self.queue.remove(highest_priority_item)

            item, priority = highest_priority_item
            self.message_label.config(text=f"Item '{item}' with priority {priority} has been dequeued.")

    def peek_item(self):
        if len(self.queue) == 0:
            self.message_label.config(text="Queue is empty.")
        else:
            highest_priority_item = max(self.queue, key=lambda x: x[1])
            item, priority = highest_priority_item
            self.message_label.config(text=f"The item '{item}' with priority {priority} is at the front of the queue.")

    def get_size(self):
        size = len(self.queue)
        self.message_label.config(text=f"The size of the queue is {size}.")

    def traverse_queue(self):
        if len(self.queue) == 0:
            self.message_label.config(text="Queue is empty.")
        else:
            items = [f"({item}, {priority})" for item, priority in self.queue]
            self.message_label.config(text=f"The items in the queue are: {', '.join(items)}")


pq_gui = PriorityQueueGUI()
