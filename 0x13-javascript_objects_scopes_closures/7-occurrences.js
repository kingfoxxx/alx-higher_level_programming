#!/usr/bin/node
//occurence in functions and list

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
