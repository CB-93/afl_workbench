from tkinter import Label, ttk, Tk
import re

# todo list specific modules to import
# todo import scidb for events


class listingPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.arrays = self.get_schemas()
        # contents
        theTree = self.makeArrayListbox()
    def get_schemas(self):
        # don't know the delimiter for output of showing all arrays
        # so just using newline for now in dev
        schema_delimiter = "\n"
        # trying to simulate output of showing all arrays
        dummy_string = f"""
        yee <color1: string, code: int>[i=0:20:0:2; j=0:40:5:1]
        haw <hmm:float,name:string>[k=0:*:0:50; m=0:*:0:2]
        """
        each_one = [
            a.strip() for a in dummy_string.strip().split(schema_delimiter)]
        # todo how to get all namespaces and their arrays in one output
        #  (using AFl probably)?
        arrays = [
            {
                "name": e.split("<")[0].strip(),
                "attributes": re.search('<(.*)>', e)[1],
                "dimensions": re.search('\[(.*)\]', e)[1]
            }
            for e in each_one
        ]
        return(arrays)
    def makeArrayListbox(self):
        treeLabel = ttk.Label(self.frame, text="Instructions:")
        treeLabel.grid(row=0, column=0, padx=10, pady=2, rowspan=2)
        treeLabel.place(relx=0.5, rely=0, anchor='n')
        thisTree = ttk.Treeview(self.root, height=600)
        thisTree.grid(row=0, column=0, padx=10, pady=3, rowspan=2)
        # Inserting items to the treeview
        # Inserting parent
        thisTree.insert('', '0', 'namespaces',
                        text='Namespaces')
        uhhh = ["namespace1", "namespace2", "namespace3"]
        # inserting namespaces
        for n in uhhh:
            thisTree.insert('namespaces', 'end', n, text=n)
            for r in self.arrays:
                r_name = f"{n}_{r['name']}"
                r_name_attributes = f"{r_name}_attributes"
                r_name_dimensions = f"{r_name}_dimensions"
                thisTree.insert(n, 'end', r_name, text=r['name'])
                thisTree.insert(r_name, 'end', r_name_attributes, text="attributes")
                thisTree.insert(r_name, 'end', r_name_dimensions, text="dimensions")
                for a in [x.strip() for x in r["attributes"].split(",")]:
                    thisTree.insert(r_name_attributes, 'end', f"{r_name_attributes}: {a}", text=a)
                for d in [x.strip() for x in r["dimensions"].split(";")]:
                    thisTree.insert(r_name_dimensions, 'end', f"{r_name_dimensions}: {d}", text=d)