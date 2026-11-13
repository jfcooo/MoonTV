const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const dir=process.argv[2];const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))){await pg.setContent('<body style="margin:0">'+fs.readFileSync(path.join(dir,f),'utf8')+'</body>');await pg.screenshot({path:path.join(dir,f.replace('.svg','.png'))});}
await b.close();})();
