from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allTrades', methods=['GET','POST'])
def allTrades():
    temp2=open('entry.txt','r')
    file_data=temp2.read()
    no_lines=0
    for ch in file_data:
        if ch == '\n':
            no_lines=no_lines+1
    print("no lines : ",no_lines)
    file = open('entry.txt','r')
    coins=[]
    strategies=[]
    targetPrices=[]
    entryPrices=[]
    stopLossPrices=[]
    entryDates=[]
    closeDates=[]
    pnls=[]
    returns=[]
    comments=[]
    for line in file:
        # print(line)
        coin,strategy,targetPrice,entryPrice,stopLossPrice,entryDate,closeDate,pnl,return1,comment = line.strip().split("<>")
        coins.append(coin)
        strategies.append(strategy)
        targetPrices.append(targetPrice)
        entryPrices.append(entryPrice)
        stopLossPrices.append(stopLossPrice)
        entryDates.append(entryDate)
        closeDates.append(closeDate)
        pnls.append(pnl)
        returns.append(return1)
        comments.append(comment)
    cards=[]
    i=0
    for i in range(no_lines):
        value={'coin': coins[i], 'strategy': strategies[i], 'targetPrice':targetPrices[i], 'entryPrice':entryPrices[i], 'stopLossPrice':stopLossPrices[i], 'entryDate':entryDates[i], 'closeDate':closeDates[i], 'pnl':pnls[i], 'return1':returns[i], 'comment':comments[i]}
        cards.append(value)
    print('hii')
    return render_template('entry.html', cards=cards)


@app.route('/dataEntry', methods=['GET','POST'])
def dataEntry():
# all entries from fronmt end
    coin = request.form['coin']
    strategy = request.form['strategy']
    entryPrice = request.form['entryPrice']
    targetPrice = request.form['targetPrice']
    stopLossPrice = request.form['stopLossPrice']
    entryDate = request.form['entryDate']
    closeDate = request.form['closeDate']
    pnl = request.form['pnl']
    returns = request.form['returns']
    comments = request.form['comments']
    #hererere
    file = open('entry.txt','a')
    file.write(coin+"<>")
    file.write(strategy+"<>")
    file.write(targetPrice+"<>")
    file.write(entryPrice+"<>")
    file.write(stopLossPrice+"<>")
    file.write(entryDate+"<>")
    file.write(closeDate+"<>")
    file.write(pnl+"<>")
    file.write(returns+"<>")
    file.write(comments)
    file.write('\n')
    file.close()
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')