const get = (key) => {
    return localStorage.getItem(key);
};

const set = (key, value) => {
  localStorage.setItem(key, value);
};

const remove = (key) => {
  localStorage.removeItem(key);
};

export default {
    get,
    set,
    remove
}
