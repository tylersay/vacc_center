import React, { useEffect, useState } from "react";
import axios from "axios";

const Booking = () => {
  const [vac_centers, setVac_Centers] = useState();
  const vac_center_url = "http://localhost:8000/api/vac_centers";

  const [form, setForm] = useState({
    vac_center: "",
    date_assigned: "",
    time_slots: "",
    first_or_second: "",
    person_name: "",
    person_nric: "",
  });
  //////////////////////////
  // fetch center information
  //////////////////////////
  useEffect(() => {
    const fetchVacCenter = async () => {
      const response = await axios.get(vac_center_url);
      const data = await response.data;
      console.log(data);
      setVac_Centers(data);
    };
    fetchVacCenter();
  }, []);

  //////////////////////////
  // create booking
  //////////////////////////
  const [booking, setBooking] = useState();
  const bookingURL = "http://localhost:8000/api/slots";
  const createBooking = (event) => {
    event.preventDefault();
    axios.post(bookingURL, form).then(() => {
      setBooking(form);
    });
  };

  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Center Name</th>
            <th>Vaccine Type</th>
            <th>Postal Code</th>
          </tr>
        </thead>
        <tbody>
          {!vac_centers || vac_centers.length <= 0 ? (
            <tr>
              <td colSpan="5" align="center">
                <b>Loading Vaccine Centers</b>
              </td>
            </tr>
          ) : (
            vac_centers.map((vac_center) => (
              <tr key={vac_center.id}>
                <td>{vac_center.center_name}</td>
                <td>{vac_center.vac_type}</td>
                <td>{vac_center.postal_code}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      <br />
      <br />
      {/* //// selection */}
      <h2>Make Booking</h2>
      <form onSubmit={() => createBooking()}>
        <label for="vac_center">Vaccination Center</label>
        {/* <selection name="vac_center" id="vac_center">
           {!vac_centers || vac_centers.length <= 0 ? (
            <b>Loading Vaccine Centers</b>
          ) : (
            vac_centers.map((vac_center) => (
              
              <option value="{vac_center.center_name}">
                {vac_center.center_name}
              </option>
              
            ))
          )} 
          </selection> */}
          <selection name="vac_center" id="vac_center">
          <option value="Suntec">Suntec</option>
          <option value="MarinaSQ">MarinaSQ</option>
          </selection>
      </form>
    </>
  );
};

export default Booking;
