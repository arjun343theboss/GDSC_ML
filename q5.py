class FloatStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "underflow"

    def print_stack(self):
        for item in self.stack[::-1]:
            print(f"{item:.4f}")

def main():
    stack = FloatStack()

    while True:
        print("\nOptions:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print all remaining elements")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            element = float(input("Enter the element to push: "))
            stack.push(element)
            print(f"{element:.4f} pushed onto the stack.")
        elif choice == "2":
            popped_element = stack.pop()
            if popped_element == "underflow":
                print("Stack underflow! Cannot pop from an empty stack.")
            else:
                print(f"Popped element: {popped_element:.4f}")
        elif choice == "3":
            print("Stack elements:")
            stack.print_stack()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
