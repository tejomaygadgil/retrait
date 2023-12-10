class Link:
    def __init__(self, msg, parent=None) -> None:
        self.msg = msg
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"msg='{self.msg}'"

    def add(self, msg):
        link = Link(msg, self)
        self.children.append(link)


class Browser:
    def __init__(self):
        self.tabs = []
        self.head = None

    def __repr__(self):
        return f"i={self.head}, tabs={self.tabs}"

    def get_head(self):
        return self.tabs[self.head]

    def set_head(self, link):
        self.tabs[self.head] = link

    def open_new(self, msg):
        link = Link(msg)
        self.tabs.append(link)
        self.head = len(self.tabs) - 1

    def forward(self, msg):
        head = self.get_head()
        head.add(msg)
        self.set_head(head.children[-1])

    def backward(self):
        head = self.get_head()
        self.set_head(head.parent)

    def open_tab(self, msg):
        head = self.get_head()
        head.add(msg)
        self.tabs.append(head.children[-1])

    def switch_tab(self, msg):
        for i, tab in enumerate(self.tabs):
            if tab.msg == msg:
                self.head = i

    def close_tab(self, msg):
        for i, tab in enumerate(self.tabs):
            if tab.msg == msg:
                del self.tabs[i]


if __name__ == "__main__":
    urls = [
        "Googled something",
        "Link 1",
        "Link 2",
        "Link 3",
        "Googled other thing",
    ]

    browser = Browser()

    browser.open_new(urls[0])
    browser.forward(urls[1])
    browser.backward()
    browser.open_tab(urls[2])
    browser.open_tab(urls[3])
    browser.switch_tab(urls[2])
    browser.forward(urls[4])
