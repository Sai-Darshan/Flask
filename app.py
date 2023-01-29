from flask import Flask, render_template, request, redirect

app =Flask(__name__,template_folder='templates2')

@app.route('/', methods=['GET',"POST"])
def home():
    if request.method=="POST":
        num1=request.form.get('num1')
        num2=request.form.get('num2')
        add=float(num1) + float(num2)
        sub=float(num1) - float(num2)
        mul=float(num1) * float(num2)
        div=float(num1) / float(num2)
        return render_template('result1.html',add=add,sub=sub,mul=mul,div=div)

    return render_template('index1.html')
if __name__=="__main__":
    app.run(debug=True)