class Link:
    def __init__(self, msg, parent) -> None:
        self.msg = msg
        self.parent = parent
        self.children = []

    def __repr__(self):
        return f"{self.msg}, parent='{self.parent.msg}', {len(self.children)} children"

    def add(self, msg):
        tab = Link(msg, self)
        self.children.append(tab)


def open_url(link, url, return_url):
    """
    Add url to Link and return new Link.
    """
    link.add(url)
    if return_url:
        return link.children[-1]


def go_back(link):
    """
    Return parent Link.
    """
    return link.parent


def get_tabs(link):
    """
    Return leaf Links.
    """
    if not link.children:
        return link
    else:
        for child in link.children:
            get_tabs(link)


if __name__ == "__main__":
    urls = ["Googled something", "Link 1" "Link 2" "Link 3" "Googled other thing"]

    t = Link(urls[0], None)  # Start: Google something
    # Open: Link 1
    t = open_url(t, urls[1], return_url=True)
    t = go_back(t)  # Go back
    open_url(t, urls[2], return_url=False)  # New tab: Link 2
    open_url(t, urls[3], return_url=False)  # New tab: Link 3
    pass  # Switch tab: Link 2
    t.add_child(4)  # Open: Google y
    pass  #
