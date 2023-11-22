import React, { useState } from "react";

const Header = ({ name = "" }) => {
  const [title, setTitle] = useState(name);
  return (
    <div className="bg-[#a52a2a] p-4">
      <input
        id={name}
        type={"text"}
        value={title}
        onChange={(e) => {
          console.log(e.target.value);
          setTitle(e.target.value);
        }}
        className="bg-[#a52a2a] focus:bg-white text-lg w-36 font-semibold rounded outline-none px-2 py-1 hover:bg-[#fffcfcdf]"
      />
    </div>
  );
};

export default Header;
