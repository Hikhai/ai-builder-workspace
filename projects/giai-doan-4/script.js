let skill = "Them ky nang moi";
const themBtn = document.querySelector(".nut-them");
const skillList = document.querySelector("ul");
const themkyNang = () => {
  const li = document.createElement("li");
  li.textContent = skill;
  skillList.appendChild(li);
}
themBtn.addEventListener("click", themkyNang);