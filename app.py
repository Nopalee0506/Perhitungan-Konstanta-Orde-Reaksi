<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Analisis Orde Reaksi</title>
</head>
<body>

<h2>Analisis Orde Reaksi Berbasis R²</h2>

<textarea id="data" rows="6" cols="30">
t,A
0,10
1,7
2,5
3,3.6
</textarea><br><br>

<button onclick="hitung()">Analisis</button>

<p id="hasil"></p>

<script>
function hitung(){
    const raw = document.getElementById("data").value.trim().split("\n");
    let t=[], A=[];

    for(let i=1;i<raw.length;i++){
        let [ti, ai] = raw[i].split(",");
        t.push(parseFloat(ti));
        A.push(parseFloat(ai));
    }

    let A0 = A[0];
    let y1 = A.map(a => Math.log(A0/a));
    let y2 = A.map(a => (1/a - 1/A0));

    function regresi(x,y){
        let n=x.length, sx=0, sy=0, sxy=0, sx2=0;
        for(let i=0;i<n;i++){
            sx+=x[i]; sy+=y[i];
            sxy+=x[i]*y[i];
            sx2+=x[i]*x[i];
        }
        let m=(n*sxy - sx*sy)/(n*sx2 - sx*sx);
        let b=(sy - m*sx)/n;

        let ssTot=0, ssRes=0;
        let yMean=sy/n;
        for(let i=0;i<n;i++){
            let yPred=m*x[i]+b;
            ssTot+=(y[i]-yMean)**2;
            ssRes+=(y[i]-yPred)**2;
        }
        let r2=1-(ssRes/ssTot);
        return {m,b,r2};
    }

    let r1=regresi(t,y1);
    let r2=regresi(t,y2);

    let orde = r1.r2 > r2.r2 ? "Orde 1" : "Orde 2";

    document.getElementById("hasil").innerHTML = `
    <b>Hasil Analisis:</b><br>
    k Orde 1 = ${r1.m.toFixed(4)} | R² = ${r1.r2.toFixed(4)}<br>
    k Orde 2 = ${r2.m.toFixed(4)} | R² = ${r2.r2.toFixed(4)}<br><br>
    <b>Reaksi mengikuti kinetika: ${orde}</b>`;
}
</script>

</body>
</html>
