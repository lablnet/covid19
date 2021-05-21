const get_country = () => {
  return "pk";
}
const importJs = (file: string) => {
  let element = document.createElement("script");
  element.setAttribute("type", "text/javascript");
  element.setAttribute("src", `data/${file}.js?v=${new Date().getTime()}`);
  document.getElementsByTagName("head")[0].appendChild(element);
}

export {
  get_country,
  importJs
}
