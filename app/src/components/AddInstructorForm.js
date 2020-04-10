import React, { useState } from "react";

const AddInstructorForm = (props) => {
  const initialFormState = { name: "", qual: "", atuiuc: "TRUE", avail: "" };
  const [instructor, setInstructor] = useState(initialFormState);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInstructor({ ...instructor, [name]: value });
    console.log(event.target);
  };

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (!instructor.name || !instructor.qual || !instructor.avail) return;
        const atuiucBool = instructor.atuiuc === "TRUE" ? 1 : 0;
        const payload = {
          name: instructor.name,
          qualifications: instructor.qual,
          atUIUC: atuiucBool,
          semesterAvailable: instructor.avail,
        };
        props.postPayload("/instructor", JSON.stringify(payload));
        setInstructor(initialFormState);
      }}
    >
      <label>name</label>
      <input
        type="text"
        name="name"
        value={instructor.name}
        onChange={handleInputChange}
      />
      <label>qualifications</label>
      <input
        type="text"
        name="qual"
        value={instructor.qual}
        onChange={handleInputChange}
      />
      <label>atUIUC</label>
      <select name="atuiuc" onChange={handleInputChange}>
        <option value="TRUE">TRUE</option>
        <option value="FALSE">FALSE</option>
      </select>
      <label>semesterAvailable</label>
      <input
        type="text"
        name="avail"
        value={instructor.avail}
        onChange={handleInputChange}
      />
      <button>Add new instructor</button>
    </form>
  );
};

export default AddInstructorForm;
