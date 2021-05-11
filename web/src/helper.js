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

  return  filtered
}

export {
  get_feed_by_province
}
