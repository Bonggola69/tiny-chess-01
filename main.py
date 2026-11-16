import json,os,sys,urllib.request as R,urllib.error as E
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
def post(p,b):
 try:
  q=R.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
  with R.urlopen(q) as s:return json.load(s)
 except E.HTTPError as x:return {"status":"bad","code":x.code}
V=(0,100,320,330,500,900,0)
P=('KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKK','ACEECGKKEKMNELNOEKNOELMNCGKLACEE','GIIIIKKKIKLMILLMIKMMIMMMILKKGIII','KKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKL','GIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJ','ECCAECCAECCAECCAGEECIGGGOOKKOQMK')
NO=(-33,-31,-18,-14,14,18,31,33);KO=(-17,-16,-15,-1,1,15,16,17);BO=(-17,-15,15,17);RO=(-16,-1,1,16);QO=BO+RO
E=[0]*1664
for v in range(-6,7):
 if v:
  for q in range(128):
   if not q&0x88:
    r=q>>4;f=q&7;E[(v+6)*128+q]=(1 if v>0 else -1)*(V[abs(v)]+(ord(P[abs(v)-1][(r if v<0 else 7-r)*4+(f if f<4 else 7-f)])-75)*5)
OF=(0,0,NO,BO,RO,QO,KO);SL=(0,0,0,1,1,1,0)
z=88172645463325252
def rnd():
 global z;z=(z*6364136223846793005+1442695040888963407)&(1<<64)-1;return z
Z=[rnd() for _ in range(1664)];YS=rnd();ZC=[rnd() for _ in range(16)];ZE=[rnd() for _ in range(8)]
B=[0]*128;S=1;C=0;Ep=-1;H=0;KW=4;KB=116;TT={};HIST={};ND=0;NB=80000;KI=[[0,0] for _ in range(64)];PATH=[]
MATE=100000
class T(Exception):pass
def X(v,s):
 global H;H^=Z[(v+6)*128+s]
def setup(fen):
 global B,S,C,Ep,H,KW,KB
 p=fen.split();B=[0]*128;C=0;Ep=-1;H=0;r=f=0
 for ch in p[0]:
  if ch=='/':r+=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:
   s=(7-r)*16+f;v='PNBRQK'.find(ch.upper())+1
   if ch.islower():v=-v
   B[s]=v
   if v==6:KW=s
   elif v==-6:KB=s
   f+=1
 S=1 if p[1]=='w' else -1;c=p[2];C=('K' in c)+2*('Q' in c)+4*('k' in c)+8*('q' in c)
 if p[3]!='-':Ep=(int(p[3][1])-1)*16+ord(p[3][0])-97
 for s in range(128):
  v=B[s]
  if v:X(v,s)
 if S<0:H^=YS
 H^=ZC[C]
 if Ep>=0:H^=ZE[Ep&7]
def att(sq,w):
 if w:
  if not (sq-15)&0x88 and B[sq-15]==1:return 1
  if not (sq-17)&0x88 and B[sq-17]==1:return 1
 else:
  if not (sq+15)&0x88 and B[sq+15]==-1:return 1
  if not (sq+17)&0x88 and B[sq+17]==-1:return 1
 for o in NO:
  t=sq+o
  if not t&0x88 and B[t]==(2 if w else -2):return 1
 for o in KO:
  t=sq+o
  if not t&0x88 and B[t]==(6 if w else -6):return 1
 for o in BO:
  t=sq+o
  while not t&0x88:
   v=B[t]
   if v:
    if v==(3 if w else -3) or v==(5 if w else -5):return 1
    break
   t+=o
 for o in RO:
  t=sq+o
  while not t&0x88:
   v=B[t]
   if v:
    if v==(4 if w else -4) or v==(5 if w else -5):return 1
    break
   t+=o
 return 0
def gen(cap):
 ms=[]
 for f in range(128):
  if f&0x88:continue
  v=B[f]
  if not v or (v>0)!=(S>0):continue
  t=abs(v)
  if t==1:
   d=16 if v>0 else -16;lr=7 if v>0 else 0;o=f+d
   def ap(o):
    if (o>>4)==lr:
     for q in (5,4,3,2):ms.append(f|o<<7|q<<14)
    else:ms.append(f|o<<7)
   if not o&0x88 and not B[o]:
    ap(o);o2=f+2*d
    if (f>>4)==(1 if v>0 else 6) and not B[o2]:ms.append(f|o2<<7|1<<17)
   for o in (f+d-1,f+d+1):
    if o&0x88:continue
    w=B[o]
    if w and (w>0)!=(v>0):ap(o)
    elif o==Ep:ms.append(f|o<<7|2<<17)
  else:
   for o in OF[t]:
    o2=f+o
    while not o2&0x88:
     w=B[o2]
     if not w:
      if not cap:ms.append(f|o2<<7)
     else:
      if (w>0)!=(v>0):ms.append(f|o2<<7)
      break
     if not SL[t]:break
     o2+=o
   if t==6 and not cap:
    e=v<0;rk=4 if v>0 else -4
    if C&(1 if v>0 else 4) and not B[f+1] and not B[f+2] and B[f+3]==rk and not att(f,e) and not att(f+1,e) and not att(f+2,e):ms.append(f|(f+2)<<7|4<<17)
    if C&(2 if v>0 else 8) and not B[f-1] and not B[f-2] and not B[f-3] and B[f-4]==rk and not att(f,e) and not att(f-1,e) and not att(f-2,e):ms.append(f|(f-2)<<7|4<<17)
 return ms
def make(m):
 global S,C,Ep,H,KW,KB
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=(m>>17)&7
 v=B[f];oh=H;oc=C;oep=Ep
 if fl&2:
  cs=t-16 if v>0 else t+16;cap=B[cs];B[cs]=0;X(cap,cs)
 else:
  cap=B[t]
  if cap:X(cap,t)
 X(v,f);B[f]=0;nv=(pr if v>0 else -pr) if pr else v;B[t]=nv;X(nv,t)
 if fl&4:
  rs=t+1 if t>f else t-2;rd=t-1 if t>f else t+1;rk=B[rs];B[rd]=rk;B[rs]=0;X(rk,rs);X(rk,rd)
 if v==6:C&=~3
 elif v==-6:C&=~12
 if f==7 or t==7:C&=~1
 if f==0 or t==0:C&=~2
 if f==119 or t==119:C&=~4
 if f==112 or t==112:C&=~8
 if C!=oc:H^=ZC[oc]^ZC[C]
 Ep=(f+t)//2 if fl&1 else -1
 if oep>=0:H^=ZE[oep&7]
 if Ep>=0:H^=ZE[Ep&7]
 H^=YS
 if v==6:KW=t
 elif v==-6:KB=t
 S=-S
 return (m,cap,oc,oep,oh)
def unmake(u):
 global S,C,Ep,H,KW,KB
 m,cap,oc,oep,oh=u;f=m&127;t=(m>>7)&127;pr=(m>>14)&7;fl=(m>>17)&7;v=B[t]
 if v==6:KW=f
 elif v==-6:KB=f
 if fl&4:
  rs=t+1 if t>f else t-2;rd=t-1 if t>f else t+1;B[rs]=B[rd];B[rd]=0
 B[f]=(1 if v>0 else -1) if pr else v;B[t]=0
 if fl&2:B[t-16 if v>0 else t+16]=cap
 elif cap:B[t]=cap
 C=oc;Ep=oep;H=oh;S=-S
def ev():
 s=0;b1=b2=0
 for q in range(128):
  if q&0x88:continue
  v=B[q]
  if not v:continue
  if abs(v)==3:
   if v>0:b1+=1
   else:b2+=1
  s+=E[(v+6)*128+q]
 if b1>1:s+=30
 if b2>1:s-=30
 for d in (15,16,17):
  q=KW+d
  if not q&0x88 and B[q]==1:s+=12
  q=KB-d
  if not q&0x88 and B[q]==-1:s-=12
 return s if S>0 else -s
def order(ms,tt,pl):
 def k(m):
  s=0
  if m==tt:s=1000000
  else:
   t=(m>>7)&127;v=B[t]
   if v:s=10000+10*V[abs(v)]-V[abs(B[m&127])]
   if (m>>14)&7:s+=9000
   if m==KI[pl][0] or m==KI[pl][1]:s+=5000
  return -s
 ms.sort(key=k);return ms
def qs(a,b,pl):
 global ND
 ND+=1
 if ND>NB:raise T
 s=ev()
 if s>=b:return b
 if s>a:a=s
 ks=KW if S>0 else KB;ck=att(ks,S<0);ms=order(gen(not ck),0,pl);lg=0
 for m in ms:
  u=make(m);ks2=KW if S<0 else KB
  if att(ks2,S>0):unmake(u);continue
  lg+=1;s=-qs(-b,-a,pl+1);unmake(u)
  if s>=b:return b
  if s>a:a=s
 return -MATE+pl if ck and not lg else a
def search(a,b,d,pl):
 global ND,S,Ep,H
 ND+=1
 if ND>NB:raise T
 if H in PATH or H in HIST:return 0
 e=TT.get(H)
 if e and e[0]>=d:
  s=e[1]
  if e[2]==0:return s
  if e[2]==1 and s>=b:return s
  if e[2]==2 and s<=a:return s
 if d<=0:return qs(a,b,pl)
 k0=KW if S>0 else KB
 if d>=3 and not att(k0,S<0) and ev()>=b:
  oS=S;oE=Ep;oH=H;S=-S;Ep=-1
  if oE>=0:H^=ZE[oE&7]
  H^=YS
  s=-search(-b,-b+1,d-3,pl+1)
  S=oS;Ep=oE;H=oH
  if s>=b:return b
 a0=a;PATH.append(H)
 try:
  ms=order(gen(False),e[3] if e else 0,pl);best=-MATE;bm=0;lg=0
  for m in ms:
   u=make(m);ks=KW if S<0 else KB
   if att(ks,S>0):unmake(u);continue
   lg+=1
   if lg==1:s=-search(-b,-a,d-1,pl+1)
   elif lg>3 and d>=3 and not u[1] and not (m>>14)&7 and m!=KI[pl][0] and m!=KI[pl][1]:
    s=-search(-a-1,-a,d-2,pl+1)
    if s>a:s=-search(-b,-a,d-1,pl+1)
   else:
    s=-search(-a-1,-a,d-1,pl+1)
    if s>a:s=-search(-b,-a,d-1,pl+1)
   unmake(u)
   if s>best:best=s;bm=m
   if s>a:a=s
   if a>=b:
    if not u[1] and not ((m>>14)&7):KI[pl][1]=KI[pl][0];KI[pl][0]=m
    break
  if not lg:
   ks=KW if S>0 else KB
   return -MATE+pl if att(ks,S<0) else 0
  fl=0
  if best<=a0:fl=2
  elif best>=b:fl=1
  TT[H]=(d,best,fl,bm)
  return best
 finally:PATH.pop()
def uci(m):
 f=m&127;t=(m>>7)&127;s="abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1);pr=(m>>14)&7
 if pr:s+="nbrq"[pr-2]
 return s
def bestmove(legal):
 global ND,PATH
 ND=0;PATH=[H];pv=0;bm=0;d=1;last=[]
 while d<=14:
  try:
   ms=order(gen(False),pv,0);a=-MATE;b=MATE;bs=-MATE;cb=0;res=[];lg=0
   for m in ms:
    u=make(m);ks=KW if S<0 else KB
    if att(ks,S>0):unmake(u);continue
    ch=H
    if lg==0:s=-search(-b,-a,d-1,1)
    else:
     s=-search(-a-1,-a,d-1,1)
     if s>a:s=-search(-b,-a,d-1,1)
    unmake(u);lg+=1;res.append((s,m,ch))
    if s>bs:bs=s;cb=m
    if s>a:a=s
   if cb:bm=cb;pv=cb;last=res
   else:break
  except T:break
  d+=1
 bs=-MATE;fm=0
 for s,m,ch in last:
  if s>bs and HIST.get(ch,0)<2:bs=s;fm=m
 if fm:
  u=make(fm);HIST[H]=HIST.get(H,0)+1;unmake(u);return uci(fm)
 return uci(bm) if bm else legal[0]
def main():
 while True:
  g=post("/game",{})
  if g.get("status")=="done":break
  if g.get("status")!="your_move":break
  setup(g["fen"]);HIST[H]=HIST.get(H,0)+1;mv=bestmove(g["legal_moves"]);h=post("/move",{"game":g["game"],"move":mv})
  if not h.get("status"):
   h=post("/move",{"game":g["game"],"move":g["legal_moves"][0]})
   if not h.get("status"):break
  g=h
main()
