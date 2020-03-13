from xml.etree.ElementTree import XMLParser


class MaxDepth:  # The target object of the parser
    maxDepth = 0
    depth = 0
    blue = 0
    red = 0
    green = 0
    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        if attrib['color'] == 'blue':
            self.blue += self.depth
        if attrib['color'] == 'red':
            self.red += self.depth
        if attrib['color'] == 'green':
            self.green += self.depth
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return [self.red, self.green, self.blue]


target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()

parser.feed(exampleXml)
for item in parser.close():
    print(item, end=" ")
