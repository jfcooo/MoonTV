const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const dir=process.argv[2],css=process.argv[3];const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg'))){const h=path.join(dir,f.replace('.svg','.html'));
fs.writeFileSync(h,'<html><head><link rel="stylesheet" href="file://'+css+'"></head><body style="margin:0">'+fs.readFileSync(path.join(dir,f),'utf8')+'</body></html>');
await pg.goto('file://'+h);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(400);await pg.evaluate(()=>document.fonts.ready);
await pg.screenshot({path:path.join(dir,f.replace('.svg','.png'))});}
await b.close();})();
