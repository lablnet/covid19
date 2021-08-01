const get_feed_by_province = (state) => {
  let filtered = []
  // eslint-disable-next-line no-undef
  let data = feed
  if (state === "all") return data
  for (let item in data) {
    let des = data[item].desc
    let words = des.split(" ")
    for (let word in words) {
      if (words[word] === state) filtered.push(data[item])
    }
  }

  return filtered
}

Object.size = function (obj) {
  var size = 0,
    key;
  for (key in obj) {
    // eslint-disable-next-line no-prototype-builtins
    if (obj.hasOwnProperty(key)) size++;
  }
  return size;
};
const object_length = (obj) => {
  return Object.size(obj)
}
const get_province_stat = (state) => {
  let data = get_feed_by_province(state)
  let size = Object.size(data)
  let filtered = []
  let i = 0
  let index = 0
  for (; ;) {
    if (index === 10) break;
    if (data[i] !== undefined && data[i].type === "INFECTED") {
      filtered.push(data[i])
      index++
    }
    i++
  }

  return filtered
}
const numFormatter = (num) => {
  if(num > 999 && num < 1000000) return ( num / 1000 ).toFixed(1) + 'K'
  else if(num > 1000000) return ( num / 1000000 ).toFixed(1) + 'M'
  else return num
}
export {
  get_feed_by_province,
  get_province_stat,
  object_length,
  numFormatter
}
