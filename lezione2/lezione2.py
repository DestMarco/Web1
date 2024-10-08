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
        .card {{
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <!-- pag11 block -->
     div id="pag11">
        <div class="container text-center">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">DArck souls dance.</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class=card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">DArck souls dance .</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">Darck souls dance .</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- pag12 block repeated N times -->
    <div id="pag12">
        <div class="container text-center">
            <div class="row">
                
    <div class="col-md-4">
        <div class="card" style="width: 18rem;">
            <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Darck souls dance.</p>
                <a href="#" class="btn btn-primary">Vai al sito</a>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card" style="width: 18rem;">
            <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Darck souls dance.</p>
                <a href="#" class="btn btn-primary">Vai al sito</a>
            </div>
        </div>
    </div>

    <div class="col-md-4">
        <div class="card" style="width: 18rem;">
            <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Darck souls dance.</p>
                <a href="#" class="btn btn-primary">Vai al sito</a>
            </div>
        </div>
    </div>

            </div>
        </div>
    </div>
    
    <!-- pag13 block -->
    <div id="pag13">
        <div class="container text-center">
            <div class="row">
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">Darck souls dance.</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">Darck souls dance.</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card" style="width: 18rem;">
                        <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
                        <div class="card-body">
                            <h5 class="card-title">Card title</h5>
                            <p class="card-text">Darck souls dance.</p>
                            <a href="#" class="btn btn-primary">Vai al sito</a>
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

pag12_card = """
    <div class="col-md-4">
        <div class="card" style="width: 18rem;">
            <img src="../img/img1_dg.gif" class="card-img-top" alt="Cane">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Darck souls dance.</p>
                <a href="#" class="btn btn-primary">Vai al sito</a>
            </div>
        </div>
    </div>
"""

pag12_content = (pag12_card * N)

final_html = html_template.format(pag12_content)

with open("generated_page.html", "w") as file:
    file.write(final_html)

print("HTML page generated successfully.")
