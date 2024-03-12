class HTMLNode:
    def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def props_to_html(self):
        if self.props != None:
            s = ""
            for k in self.props:
                s += f" {k}=\"{self.props[k]}\""
            return s
        else:
            return ""
    def __repr__(self):
        return f"HTMLNode{self.tag,self.value,self.children,self.props}"

class LeafNode(HTMLNode):
    def __init__(self,tag:str, value:str ,props:dict = None):
        super().__init__(tag,value,None, props)
    def to_html(self):
        
        if self.value == None:
            raise ValueError("All leaf nodes require a value.")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode{self.tag,self.value,self.props}"
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list,props: dict = None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if len(self.children) != 0:
            s = ""
            for c in self.children:
                if c.tag == None:
                    s += c.value
                else:
                    s += f"{c.to_html()}"
            return f"<{self.tag}>{s}</{self.tag}>"
        else:
            raise ValueError("Given node has no children.")
    def __repr__(self):
        return f"ParentNode{self.tag,self.children,self.props}"
        
