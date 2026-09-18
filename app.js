const parts = {
  cpu: [
    ["Intel Core i3-10100",34,65],["Intel Core i5-10400F",43,65],["Intel Core i5-11400F",49,65],
    ["Intel Core i5-12400F",64,65],["Intel Core i5-12600K",76,125],["Intel Core i5-13400F",73,65],
    ["Intel Core i5-13600K",88,125],["Intel Core i5-14400F",76,65],["Intel Core i5-14600K",91,125],
    ["Intel Core i7-12700K",84,125],["Intel Core i7-13700K",93,125],["Intel Core i7-14700K",97,125],
    ["Intel Core i9-12900K",89,125],["Intel Core i9-13900K",98,125],["Intel Core i9-14900K",100,125],
    ["AMD Ryzen 3 3100",32,65],["AMD Ryzen 5 3600",46,65],["AMD Ryzen 5 5500",49,65],
    ["AMD Ryzen 5 5600",61,65],["AMD Ryzen 5 5600X",64,65],["AMD Ryzen 5 7600",76,65],
    ["AMD Ryzen 5 7600X",79,105],["AMD Ryzen 5 9600X",88,65],["AMD Ryzen 7 5700X",69,65],
    ["AMD Ryzen 7 5800X3D",81,105],["AMD Ryzen 7 7700X",85,105],["AMD Ryzen 7 7800X3D",96,120],
    ["AMD Ryzen 7 9700X",93,65],["AMD Ryzen 7 9800X3D",100,120],["AMD Ryzen 9 5900X",77,105],
    ["AMD Ryzen 9 7900X",92,170],["AMD Ryzen 9 7950X3D",99,120]
  ],
  gpu: [
    ["NVIDIA GTX 1060 6GB",25,120],["NVIDIA GTX 1660 Super",34,125],["NVIDIA RTX 2060",39,160],
    ["NVIDIA RTX 3060 12GB",50,170],["NVIDIA RTX 3060 Ti",59,200],["NVIDIA RTX 3070",66,220],
    ["NVIDIA RTX 3080",79,320],["NVIDIA RTX 3090",84,350],["NVIDIA RTX 4060",52,115],
    ["NVIDIA RTX 4060 Ti",62,160],["NVIDIA RTX 4070",74,200],["NVIDIA RTX 4070 Super",81,220],
    ["NVIDIA RTX 4070 Ti Super",88,285],["NVIDIA RTX 4080 Super",95,320],["NVIDIA RTX 4090",100,450],
    ["NVIDIA RTX 5070",84,250],["NVIDIA RTX 5080",97,360],["NVIDIA RTX 5090",115,575],
    ["AMD RX 580 8GB",23,185],["AMD RX 5600 XT",37,150],["AMD RX 6600",45,132],
    ["AMD RX 6700 XT",61,230],["AMD RX 6800 XT",76,300],["AMD RX 7600",52,165],
    ["AMD RX 7700 XT",69,245],["AMD RX 7800 XT",78,263],["AMD RX 7900 GRE",83,260],
    ["AMD RX 7900 XT",91,315],["AMD RX 7900 XTX",97,355],["Intel Arc A580",45,185],
    ["Intel Arc A750",49,225],["Intel Arc B580",57,190]
  ]
};

const $ = s => document.querySelector(s);
const clamp = (n,min=0,max=100) => Math.max(min, Math.min(max, Math.round(n)));

function fillSelect(id,list,selected){
  const el=$(id);
  if(!el) return;
  list.forEach((p,i)=>{
    const option=document.createElement("option");
    option.value=i; option.textContent=p[0];
    if(p[0]===selected) option.selected=true;
    el.append(option);
  });
}

function setMeter(name,value){
  const text=$(name+"Text"), bar=$(name+"Bar");
  if(text) text.textContent=value+"%";
  if(bar) bar.style.width=value+"%";
}

function analyze(){
  const cpu=parts.cpu[+$("#cpu").value], gpu=parts.gpu[+$("#gpu").value];
  const res=+$("#resolution").value, workload=$("#workload").value;
  const ram=+$("#ram").value, storage=$("#storage").value;
  const temp=+$("#temperature").value, psu=+$("#psu").value;
  const resGpu={1080:.78,1440:1,2160:1.27}[res];
  const useCpu={gaming:1.08,creative:.96,office:.72,mixed:.90}[workload];
  const targetGpu=gpu[1]*resGpu, targetCpu=cpu[1]*useCpu;
  const gap=Math.abs(targetCpu-targetGpu)/Math.max(targetCpu,targetGpu);
  const balance=clamp(100-gap*105);
  const ramNeed=workload==="creative"?32:(workload==="gaming"||workload==="mixed"?16:8);
  const ramScore=clamp(62+(ram/ramNeed)*28-(ram<ramNeed?18:0));
  const thermal=clamp(100-Math.max(0,temp-60)*2.25);
  const drive={hdd:58,sata:82,nvme:96}[storage];
  const demand=(cpu[2]+gpu[2]+90)*1.3;
  const power=clamp(100-Math.max(0,demand-psu)/5);
  const score=clamp(balance*.38+ramScore*.16+thermal*.20+power*.17+drive*.09);
  const cpuLimited=targetCpu<targetGpu;
  let verdict,copy,tip;
  if(balance>=82){
    verdict="Healthy & balanced"; copy="Your selected CPU and GPU are a sensible match for this target.";
    tip=thermal<65?"Improve airflow or cooling before upgrading hardware.":power<70?"Check PSU quality and capacity before sustained heavy loads.":"No urgent core upgrade. Focus on maintenance, drivers and game settings.";
  }else if(cpuLimited){
    verdict="CPU-limited scenario"; copy=cpu[0]+" may limit "+gpu[0]+" in this workload.";
    tip="Prioritize a faster CPU/platform, or raise resolution and visual settings to use more GPU capacity.";
  }else{
    verdict="GPU-limited scenario"; copy=gpu[0]+" is the likely performance ceiling at this resolution.";
    tip="A graphics-card upgrade may provide the clearest gain; lowering demanding visual settings can help now.";
  }
  if(ramScore<65) tip="Increase memory to at least "+ramNeed+" GB and use a matched dual-channel kit where supported.";
  if(thermal<50) tip="Address temperatures first: clean dust, verify fans and cooler mounting, then retest.";
  if(power<55) tip="Check PSU capacity, quality, connectors and component requirements before increasing load.";

  $("#scoreRing").style.setProperty("--score",score);
  $("#scoreValue").textContent=score; $("#verdict").textContent=verdict; $("#verdictText").textContent=copy;
  const max=Math.max(targetCpu,targetGpu,100);
  $("#cpuTower").style.setProperty("--height",clamp(targetCpu/max*100,22,100)+"%");
  $("#gpuTower").style.setProperty("--height",clamp(targetGpu/max*100,22,100)+"%");
  $("#cpuName").textContent=cpu[0].replace("AMD ","").replace("Intel ","");
  $("#gpuName").textContent=gpu[0].replace("NVIDIA ","").replace("AMD ","");
  $("#cpuIndex").textContent="Adjusted CPU index "+Math.round(targetCpu);
  $("#gpuIndex").textContent="Adjusted GPU index "+Math.round(targetGpu);
  $("#cpuScore").textContent=Math.round(targetCpu); $("#gpuScore").textContent=Math.round(targetGpu);
  $("#limitLabel").textContent=balance>=82?"Balanced pairing":cpuLimited?"CPU is the likely limit":"GPU is the likely limit";
  $("#factResolution").textContent=res===2160?"4K":res+"p";
  $("#factPower").textContent=Math.round(demand)+" W";
  $("#factStorage").textContent={hdd:"HDD",sata:"SATA SSD",nvme:"NVMe SSD"}[storage];
  setMeter("#balance",balance); setMeter("#ram",ramScore); setMeter("#thermal",thermal); setMeter("#power",power);
  $("#advice").innerHTML="<b>Next step:</b> "+tip;
}

function setup(){
  fillSelect("#cpu",parts.cpu,"AMD Ryzen 5 7600X");
  fillSelect("#gpu",parts.gpu,"NVIDIA RTX 4070");
  const form=$("#calculatorForm");
  if(form){ form.addEventListener("submit",e=>{e.preventDefault();analyze(); $("#calculator").scrollIntoView({behavior:"smooth",block:"start"});}); analyze(); }
  const temp=$("#temperature"), psu=$("#psu");
  if(temp) temp.addEventListener("input",()=>$("#temperatureValue").textContent=temp.value+"°C");
  if(psu) psu.addEventListener("input",()=>$("#psuValue").textContent=psu.value+" W");
  const root=document.documentElement, theme=$("#themeButton");
  const saved=localStorage.getItem("pc-theme");
  if(saved) root.dataset.theme=saved;
  if(theme) theme.textContent=root.dataset.theme==="dark"?"☀":"☾";
  if(theme) theme.addEventListener("click",()=>{root.dataset.theme=root.dataset.theme==="dark"?"light":"dark";localStorage.setItem("pc-theme",root.dataset.theme);theme.textContent=root.dataset.theme==="dark"?"☀":"☾";});
  const menu=$("#menuButton"), nav=$("#mainNav");
  if(menu&&nav) menu.addEventListener("click",()=>{const open=nav.classList.toggle("open");menu.setAttribute("aria-expanded",open);});
  const year=$("#year"); if(year) year.textContent=new Date().getFullYear();
}
document.addEventListener("DOMContentLoaded",setup);
