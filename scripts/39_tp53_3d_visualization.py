import py3Dmol

pdb_file = "../data/2XWR.pdb"

with open(pdb_file, "r") as file:
    structure_data = file.read()

view = py3Dmol.view(width=1000, height=750)

view.addModel(structure_data, "cif")

# Hide everything first
view.setStyle({}, {"hidden": True})

# Show only TP53 chain A
view.setStyle(
    {"chain": "A"},
    {"cartoon": {"color": "lightblue"}}
)

mutation_data = {
    175: "R175H",
    179: "H179R",
    220: "Y220C",
    248: "R248W",
    273: "R273H",
    280: "R280K",
    282: "R282W"
}

# Highlight mutation positions
for position, mutation in mutation_data.items():

    view.addStyle(
        {
            "chain": "A",
            "resi": position
        },
        {
            "stick": {
                "color": "red",
                "radius": 0.25
            },
            "sphere": {
                "color": "red",
                "radius": 0.8
            }
        }
    )

    view.addLabel(
        mutation,
        {
            "fontSize": 14,
            "fontColor": "black",
            "backgroundColor": "white",
            "backgroundOpacity": 0.8,
            "showBackground": True
        },
        {
            "chain": "A",
            "resi": position
        }
    )

view.zoomTo({"chain": "A"})

view.write_html(
    "../figures/TP53_3D_Mutation_Structure.html"
)

print("Clean 3D TP53 visualization created.")
print("Saved to: ../figures/TP53_3D_Mutation_Structure.html")