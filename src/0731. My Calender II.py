class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.already_booked = []

    def book(self, start: int, end: int) -> bool:

        for event_start, event_end in self.already_booked:

            if start < event_end and event_start < end:
                return False

        for event_start, event_end in self.events:
            if start < event_end and end > event_start:
                self.already_booked.append((max(start, event_start), min(end, event_end)))

        self.events.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)