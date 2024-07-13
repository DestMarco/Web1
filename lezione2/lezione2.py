N = 3

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Layout with Bootstrap</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            text-align: center;
        }}
    </style>
</head>
<body>
    <!-- pag11 block -->
    <div id="pag11">
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            Pag11 - Card 1
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            Pag11 - Card 2
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- pag12 block repeated N times -->
    <div id="pag12">
        {}
    </div>
    
    <!-- pag13 block -->
    <div id="pag13">
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">
                            Pag13 - Card 1
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""

pag12_block = """
<div class="container">
    <div class="row">
        <div class="col">
            <div class="card">
                <div class="card-body">
                    Pag12 - Card 1
                </div>
            </div>
        </div>
        <div class="col">
            <div class="card">
                <div class="card-body">
                    Pag12 - Card 2
                </div>
            </div>
        </div>
        <div class="col">
            <div class="card">
                <div class="card-body">
                    Pag12 - Card 3
                </div>
            </div>
        </div>
    </div>
</div>
"""

pag12_content = pag12_block * N
final_html = html_template.format(pag12_content)

with open("generated_page.html", "w") as file:
    file.write(final_html)

print("HTML page generated successfully.")