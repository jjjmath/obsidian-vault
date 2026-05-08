
### 点




<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
 <circle cx="100" cy="100" r="5" fill="red"/>
</svg>
### 线
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
 <line x1="50" y1="100" x2="200" y2="100" stroke="black" stroke-width="2"/>
</svg>
### 折线

<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
<polyline points="50,150 100,120 150,140 200,110" fill="none" stroke="blue" stroke-width="2"/>
</svg>
### 矩形

<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="200" width="100" height="60" fill="none" stroke="black"/>
</svg>
### 圆和椭圆

<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
<circle cx="200" cy="100" r="30" fill="red"/>
<ellipse cx="300" cy="100" rx="50" ry="25" fill="blue"/>

</svg>

### 多边形

<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
<!-- 三角形 -->
<polygon points="100,250 50,300 150,300" fill="yellow" stroke="black"/>
<path d="M 100,100 L 200,100 L 150,200 Z" fill="green"/>


</svg>
### 完整示例
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">

 
 <!-- 三角形 -->
 <polygon points="100,200 200,100 300,200" 
 fill="#3498db" fill-opacity="0.3" 
 stroke="#3498db" stroke-width="2"/>
 
 <!-- 顶点 -->
 <circle cx="100" cy="200" r="4" fill="#e74c3c"/>
 <circle cx="200" cy="100" r="4" fill="#e74c3c"/>
 <circle cx="300" cy="200" r="4" fill="#e74c3c"/>
 
 <!-- 标签 -->
 <text x="90" y="220" font-size="14">A</text>
 <text x="195" y="90" font-size="14">B</text>
 <text x="305" y="220" font-size="14">C</text>
</svg>

</svg>

### 正方体
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
 
 <!-- ===== 正面（长×宽）===== -->
 <polygon points="100,180 220,180 220,300 100,300"
 fill="#3498db" fill-opacity="0" stroke="#3498db" stroke-width="2"/>
 
 <!-- ===== 顶面（长×高）===== -->
 <polygon points="100,180 220,180 300,120 180,120"
 fill="#2ecc71" fill-opacity="0" stroke="#2ecc71" stroke-width="2"/>
 
 <!-- ===== 右侧面（宽×高）===== -->
 <polygon points="220,180 220,300 300,240 300,120"
 fill="#e74c3c" fill-opacity="0" stroke="#e74c3c" stroke-width="2"/>
 
 <!-- ===== 与H相连的虚线边 ===== -->
 <!-- AH（左下前到左上下） -->
 <line x1="100" y1="300" x2="180" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <!-- HE（左上下到左上后） -->
 <line x1="180" y1="240" x2="180" y2="120" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <!-- HG（左上下到右上下） -->
 <line x1="180" y1="240" x2="300" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 
 <!-- ===== 顶点标记（8个点）===== -->
 <circle cx="100" cy="300" r="4" fill="#333"/> <!-- A -->
 <circle cx="220" cy="180" r="4" fill="#333"/> <!-- B -->
 <circle cx="220" cy="300" r="4" fill="#333"/> <!-- C -->
 <circle cx="100" cy="180" r="4" fill="#333"/> <!-- D -->
 <circle cx="180" cy="120" r="4" fill="#333"/> <!-- E -->
 <circle cx="300" cy="120" r="4" fill="#333"/> <!-- F -->
 <circle cx="300" cy="240" r="4" fill="#333"/> <!-- G -->
 <circle cx="180" cy="240" r="4" fill="#333"/> <!-- H -->
 
 <!-- ===== 顶点标签 ===== -->
 <text x="90" y="320" font-size="16" font-weight="bold" fill="#333">A</text>
 <text x="220" y="175" font-size="16" font-weight="bold" fill="#333">B</text>
 <text x="225" y="315" font-size="16" font-weight="bold" fill="#333">C</text>
 <text x="85" y="175" font-size="16" font-weight="bold" fill="#333">D</text>
 <text x="170" y="115" font-size="16" font-weight="bold" fill="#333">E</text>
 <text x="305" y="115" font-size="16" font-weight="bold" fill="#333">F</text>
 <text x="305" y="240" font-size="16" font-weight="bold" fill="#333">G</text>
 <text x="175" y="235" font-size="16" font-weight="bold" fill="#333">H</text>
 
</svg>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
 
 <!-- ===== 正面（长×宽）===== -->
 <polygon points="100,180 220,180 220,300 100,300"
 fill="#3498db" fill-opacity="0" stroke="#3498db" stroke-width="2"/>
 
 <!-- ===== 顶面（长×高）===== -->
 <polygon points="100,180 220,180 300,120 180,120"
 fill="#2ecc71" fill-opacity="0" stroke="#2ecc71" stroke-width="2"/>
 
 <!-- ===== 右侧面（宽×高）===== -->
 <polygon points="220,180 220,300 300,240 300,120"
 fill="#e74c3c" fill-opacity="0" stroke="#e74c3c" stroke-width="2"/>
 
 <!-- ===== 与H(新D)相连的虚线边 ===== -->
 <!-- A到D -->
 <line x1="100" y1="300" x2="180" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <!-- D到D1 -->
 <line x1="180" y1="240" x2="180" y2="120" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <!-- D到C -->
 <line x1="180" y1="240" x2="300" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 
 <!-- ===== 顶点标记（8个点）===== -->
 <circle cx="100" cy="300" r="4" fill="#333"/> <!-- A -->
 <circle cx="220" cy="300" r="4" fill="#333"/> <!-- B (原C) -->
 <circle cx="300" cy="240" r="4" fill="#333"/> <!-- C (原G) -->
 <circle cx="180" cy="240" r="4" fill="#333"/> <!-- D (原H) -->
 <circle cx="100" cy="180" r="4" fill="#333"/> <!-- A1 (原D) -->
 <circle cx="220" cy="180" r="4" fill="#333"/> <!-- B1 (原B) -->
 <circle cx="300" cy="120" r="4" fill="#333"/> <!-- C1 (原F) -->
 <circle cx="180" cy="120" r="4" fill="#333"/> <!-- D1 (原E) -->
 
 <!-- ===== 顶点标签（LaTeX下标格式）===== -->
 <text x="90" y="320" font-size="16" font-weight="bold" fill="#333">A</text>
 <text x="225" y="315" font-size="16" font-weight="bold" fill="#333">B</text>
 <text x="305" y="240" font-size="16" font-weight="bold" fill="#333">C</text>
 <text x="175" y="235" font-size="16" font-weight="bold" fill="#333">D</text>
 <text x="75" y="175" font-size="16" font-weight="bold" fill="#333">A<tspan dy="5" font-size="11">1</tspan></text>
 <text x="215" y="170" font-size="16" font-weight="bold" fill="#333">B<tspan dy="5" font-size="11">1</tspan></text>
 <text x="305" y="115" font-size="16" font-weight="bold" fill="#333">C<tspan dy="5" font-size="11">1</tspan></text>
 <text x="165" y="115" font-size="16" font-weight="bold" fill="#333">D<tspan dy="5" font-size="11">1</tspan></text>
 
</svg>




<svg width="400" height="250" xmlns="http://www.w3.org/2000/svg">
 
 <!-- ===== 椭圆：一半实线，一半虚线 ===== -->
 
 <!-- 上半弧（实线） -->
 <path d="M 100,125 A 100,50 0 0,0 300,125"
 fill="none" stroke="#3498db" stroke-width="3"/>
 
 <!-- 下半弧（虚线） -->
 <path d="M 100,125 A 100,50 0 0,1 300,125"
 fill="none" stroke="#3498db" stroke-width="3" stroke-dasharray="8,6"/>
 
 
</svg>


<svg width="400" height="250" xmlns="http://www.w3.org/2000/svg">
 
 <!-- ===== 椭圆：一半实线，一半虚线 ===== -->
 
 <!-- 上半弧（实线） -->
 <path d="M 100,125 A 100,50 0 0,1 300,125"
 fill="none" stroke="#3498db" stroke-width="3"/>
 
 <!-- 下半弧（虚线） -->
 <path d="M 100,125 A 100,50 0 0,0 300,125"
 fill="none" stroke="#3498db" stroke-width="3" stroke-dasharray="8,6"/>
 
 <!-- 中心点和轴线（辅助线） -->
 <line x1="300" y1="125" x2="100" y2="125" stroke="#999" stroke-width="1" stroke-dasharray="4,4"/>
 <line x1="200" y1="75" x2="200" y2="175" stroke="#999" stroke-width="1" stroke-dasharray="4,4"/>
 <circle cx="200" cy="125" r="3" fill="#333"/>
 
 <!-- 标注 -->
 <text x="200" y="195" text-anchor="middle" font-size="14" fill="#666">上半弧：实线</text>
 <text x="200" y="215" text-anchor="middle" font-size="14" fill="#666">下半弧：虚线</text>
 
</svg>
<svg width="500" height="450" xmlns="http://www.w3.org/2000/svg">
 
 <!-- 正面 A-B-B1-A1 -->
 <polygon points="100,300 300,300 300,180 100,180"
 fill="#3498db" fill-opacity="0" stroke="#3498db" stroke-width="2"/>
 
 <!-- 顶面 A1-B1-C1-D1 -->
 <polygon points="100,180 300,180 380,120 180,120"
 fill="#2ecc71" fill-opacity="0" stroke="#2ecc71" stroke-width="2"/>
 
 <!-- 右侧面 B-B1-C1-C -->
 <polygon points="300,300 300,180 380,120 380,240"
 fill="#e74c3c" fill-opacity="0" stroke="#e74c3c" stroke-width="2"/>
 
 <!-- 虚线：A→D, D→D1, D→C -->
 <line x1="100" y1="300" x2="171" y2="229" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <line x1="171" y1="229" x2="180" y2="120" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <line x1="171" y1="229" x2="380" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 
 <!-- 顶点 -->
 <circle cx="100" cy="300" r="4" fill="#333"/> <!-- A   -->
 <circle cx="300" cy="300" r="4" fill="#333"/> <!-- B   -->
 <circle cx="380" cy="240" r="4" fill="#333"/> <!-- C   -->
 <circle cx="171" cy="229" r="4" fill="#333"/> <!-- D   -->
 <circle cx="100" cy="180" r="4" fill="#333"/> <!-- A₁  -->
 <circle cx="300" cy="180" r="4" fill="#333"/> <!-- B₁  -->
 <circle cx="380" cy="120" r="4" fill="#333"/> <!-- C₁  -->
 <circle cx="180" cy="120" r="4" fill="#333"/> <!-- D₁  -->

 <!-- 标签（完全保持你的格式） -->
 <text x="90" y="320" font-size="16" font-weight="bold" fill="#333">A</text>
 <text x="305" y="315" font-size="16" font-weight="bold" fill="#333">B</text>
 <text x="385" y="240" font-size="16" font-weight="bold" fill="#333">C</text>
 <text x="155" y="225" font-size="16" font-weight="bold" fill="#333">D</text>
 <text x="80" y="175" font-size="16" font-weight="bold" fill="#333">A<tspan dy="5" font-size="11">1</tspan></text>
 <text x="295" y="170" font-size="16" font-weight="bold" fill="#333">B<tspan dy="5" font-size="11">1</tspan></text>
 <text x="385" y="115" font-size="16" font-weight="bold" fill="#333">C<tspan dy="5" font-size="11">1</tspan></text>
 <text x="165" y="115" font-size="16" font-weight="bold" fill="#333">D<tspan dy="5" font-size="11">1</tspan></text>

</svg>
<svg width="500" height="450" xmlns="http://www.w3.org/2000/svg">
 
 <!-- 正面 A-B-B₁-A₁ -->
 <polygon points="100,300 260,300 260,140 100,140"
 fill="#3498db" fill-opacity="0" stroke="#3498db" stroke-width="2"/>
 
 <!-- 顶面 A₁-B₁-C₁-D₁ -->
 <polygon points="100,140 260,140 340,80 180,80"
 fill="#2ecc71" fill-opacity="0" stroke="#2ecc71" stroke-width="2"/>
 
 <!-- 右侧面 B-B₁-C₁-C -->
 <polygon points="260,300 260,140 340,80 340,240"
 fill="#e74c3c" fill-opacity="0" stroke="#e74c3c" stroke-width="2"/>
 
 <!-- 虚线：A→D, D→D₁, D→C -->
 <line x1="100" y1="300" x2="180" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <line x1="180" y1="240" x2="180" y2="80" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 <line x1="180" y1="240" x2="340" y2="240" stroke="#333" stroke-width="2" stroke-dasharray="5,5"/>
 
 <!-- 顶点 -->
 <circle cx="100" cy="300" r="2" fill="#333"/> <!-- A   -->
 <circle cx="260" cy="300" r="2" fill="#333"/> <!-- B   -->
 <circle cx="340" cy="240" r="2" fill="#333"/> <!-- C   -->
 <circle cx="180" cy="240" r="2" fill="#333"/> <!-- D   -->
 <circle cx="100" cy="140" r="2" fill="#333"/> <!-- A₁  -->
 <circle cx="260" cy="140" r="2" fill="#333"/> <!-- B₁  -->
 <circle cx="340" cy="80" r="2" fill="#333"/>  <!-- C₁  -->
 <circle cx="180" cy="80" r="2" fill="#333"/>  <!-- D₁  -->

 <!-- 标签 -->
 <text x="85" y="320" font-size="16" font-weight="bold" fill="#333">A</text>
 <text x="265" y="315" font-size="16" font-weight="bold" fill="#333">B</text>
 <text x="345" y="245" font-size="16" font-weight="bold" fill="#333">C</text>
 <text x="165" y="235" font-size="16" font-weight="bold" fill="#333">D</text>
 <text x="80" y="135" font-size="16" font-weight="bold" fill="#333">A<tspan dy="5" font-size="11">1</tspan></text>
 <text x="255" y="130" font-size="16" font-weight="bold" fill="#333">B<tspan dy="5" font-size="11">1</tspan></text>
 <text x="340" y="75" font-size="16" font-weight="bold" fill="#333">C<tspan dy="5" font-size="11">1</tspan></text>
 <text x="165" y="75" font-size="16" font-weight="bold" fill="#333">D<tspan dy="5" font-size="11">1</tspan></text>

</svg>

<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300">
  
  <!-- 背景（可选，白色） -->
  <rect width="600" height="300" fill="white"/>
  
  <!-- 坐标系变换：数学 y 轴向上，SVG y 轴向下 -->
  <!-- 原点在 (50, 150)，x 向右，y 向上 -->
  <g transform="translate(50, 150)">
    
    <!-- x 轴（水平向右）-->
    <line x1="-20" y1="0" x2="560" y2="0" stroke="black" stroke-width="2"/>
    <polygon points="560,-5 560,5 575,0" fill="black"/>
    <text x="560" y="-10" font-size="14" fill="black" font-family="serif">x</text>
    
    <!-- y 轴（垂直向上）-->
    <line x1="0" y1="-130" x2="0" y2="130" stroke="black" stroke-width="2"/>
    <polygon points="-5,-130 5,-130 0,-145" fill="black"/>
    <text x="10" y="-140" font-size="14" fill="black" font-family="serif">y</text>
    
    <!-- 原点 O -->
    <circle cx="0" cy="0" r="3" fill="black"/>
    <text x="5" y="-5" font-size="13" fill="black" font-family="serif">O</text>
    
    <!-- x 轴刻度：0, π/2, π, 3π/2, 2π -->
    <!-- π/2 ≈ 1.57 → 1.57×50 ≈ 78.5 -->
    <!-- π ≈ 3.14 → 157 -->
    <!-- 3π/2 ≈ 4.71 → 235.5 -->
    <!-- 2π ≈ 6.28 → 314 -->
    
    <!-- π/2 -->
    <line x1="78.5" y1="-5" x2="78.5" y2="5" stroke="black" stroke-width="1.5"/>
    <text x="78.5" y="20" font-size="12" fill="black" font-family="serif" text-anchor="middle">π/2</text>
    
    <!-- π -->
    <line x1="157" y1="-5" x2="157" y2="5" stroke="black" stroke-width="1.5"/>
    <text x="157" y="20" font-size="12" fill="black" font-family="serif" text-anchor="middle">π</text>
    
    <!-- 3π/2 -->
    <line x1="235.5" y1="-5" x2="235.5" y2="5" stroke="black" stroke-width="1.5"/>
    <text x="235.5" y="20" font-size="12" fill="black" font-family="serif" text-anchor="middle">3π/2</text>
    
    <!-- 2π -->
    <line x1="314" y1="-5" x2="314" y2="5" stroke="black" stroke-width="1.5"/>
    <text x="314" y="20" font-size="12" fill="black" font-family="serif" text-anchor="middle">2π</text>
    
    <!-- y 轴刻度：1 和 -1 -->
    <line x1="-5" y1="-100" x2="5" y2="-100" stroke="black" stroke-width="1.5"/>
    <text x="-10" y="-96" font-size="12" fill="black" font-family="serif" text-anchor="end">1</text>
    
    <line x1="-5" y1="100" x2="5" y2="100" stroke="black" stroke-width="1.5"/>
    <text x="-10" y="104" font-size="12" fill="black" font-family="serif" text-anchor="end">-1</text>
    
    <!-- 虚线辅助线：y=1 和 y=-1 -->
    <line x1="0" y1="-100" x2="314" y2="-100" stroke="gray" stroke-width="0.8" stroke-dasharray="6,4"/>
    <line x1="0" y1="100" x2="314" y2="100" stroke="gray" stroke-width="0.8" stroke-dasharray="6,4"/>
    
    <!-- 正弦曲线 y = sin(x)，x 从 0 到 2π -->
    <!-- 使用路径，y 取负因为 SVG y 轴向下 -->
    <path d="M 0,0
             C 20,-30 50,-95 78.5,-100
             C 110,-95 140,-30 157,0
             C 180,30 210,95 235.5,100
             C 260,95 290,30 314,0"
          fill="none" stroke="#e74c3c" stroke-width="2.5" stroke-linecap="round"/>
    
    <!-- 也可以精确采样画点，曲线用更平滑的贝塞尔 -->
    
  </g>
  
</svg>
