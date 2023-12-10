class Link:
    def __init__(self, msg, parent=None) -> None:
        self.msg = msg
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"msg='{self.msg}'"

    def add_link(self, msg):
        link = Link(msg, self)
        self.children.append(link)


class Browser:
    def __init__(self):
        self.root = Link("root")
        self.tabs = [self.root]
        self.head = 0

    def __repr__(self):
        return f"i={self.head}, tabs={self.tabs}"

    def current_tab(self) -> Link:
        return self.tabs[self.head]

    def add_tab(self, link) -> None:
        self.tabs.append(link)

    def update_tab(self, link) -> None:
        assert type(link) is Link, "Insert link"
        self.tabs[self.head] = link

    def forward(self, msg, bg=False):
        tab = self.current_tab()
        tab.add_link(msg)
        new_link = tab.children[-1]
        if bg:
            self.add_tab(new_link)
        else:
            self.update_tab(new_link)

    def new_tab(self, bg=False):
        self.forward("New tab", bg)

    def backward(self):
        new_link = self.current_tab().parent
        self.update_tab(new_link)

    def switch_tab(self, msg):
        for i, tab in enumerate(self.tabs):
            if tab.msg == msg:
                self.head = i

    # def close_tab(self, msg):
    #    for i, tab in enumerate(self.tabs):
    #        if tab.msg == msg:
    #            del self.tabs[i]

    def find(self, msg):
        def recursive_search(link, msg):
            result = []
            if link.msg == msg:
                result.append(link)
            if link.children:
                for child in link.children:
                    result.extend(recursive_search(child, msg))

            return result

        return recursive_search(self.root, msg)


if __name__ == "__main__":
    urls = [
        "Googled something",
        "Link 1",
        "Link 2",
        "Link 3",
        "Googled other thing",
    ]

    browser = Browser()
    browser.new_tab()
    browser.forward(urls[0])
    browser.forward(urls[1])
    browser.backward()
    browser.forward(urls[2], bg=True)
    browser.forward(urls[3], bg=True)
    browser.switch_tab(urls[2])
    browser.forward(urls[4])
    browser.forward(urls[2])
    print(browser.find(urls[2]))
