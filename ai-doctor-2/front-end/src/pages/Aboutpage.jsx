import React from 'react';
import '../bootstrap-5.3.3-dist/css/bootstrap.css';

const Aboutpage = () => {
  return (
    <div>
      <div className="container py-5">
        <div className="row align-items-center justify-content-center g-5">
          <div className="col-md-6 text-md-start text-center">
            <h2 className="display-6 fw-bold">Serving people for more than 20+ Years</h2>
            <p className="fs-5">
              Exceptuer sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
            <p className=" fs-5">
              Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.
            </p>
            <button

              className="d-lg-inline btn btn-primary px-4 py-2 rounded-pill fw-semibold readmore"
            >
              Read More
            </button>
          </div>
          <div className="col-md-6 position-relative">
            <img
              src="https://images.pexels.com/photos/30073669/pexels-photo-30073669.jpeg"
              alt="Medical team performing surgery"
              className="img-fluid rounded shadow"
              style={{ borderRadius: '12px' }}
            />
            <div
              className="position-absolute bottom-0 start-0 m-3 bg-primary text-white p-2 rounded fw-bold"
              style={{ borderRadius: '6px' }}
            >
              Serving 20+ Years
            </div>
          </div>
        </div>
      </div>
      <div className="bg-dark text-white py-5 rounded-top">
        <div className="container">
          <div className="row justify-content-around text-center">
            <div className="col-md-4 col-lg-3 mb-4 mb-lg-0">
              <div className="custom-card p-4 rounded shadow-lg" style={{ backgroundColor: '#2a2d3e', color: 'white', border: '1px solid #444', transition: '0.3s' }}>
                <div className="fs-1 mb-3">👨‍⚕️</div>
                <h3 className="h5 mb-2">Experienced Doctors</h3>
                <p className="text-light">
                  Highly qualified doctors with years of expertise ensuring top-notch healthcare.
                </p>
              </div>
            </div>
            <div className="col-md-4 col-lg-3 mb-4 mb-lg-0">
              <div className="custom-card p-4 rounded shadow-lg" style={{ backgroundColor: '#2a2d3e', color: 'white', border: '1px solid #444', transition: '0.3s' }}>
                <div className="fs-1 mb-3">🛠️</div>
                <h3 className="h5 mb-2">Latest Technology</h3>
                <p className="text-light">
                  Cutting-edge medical technology for accurate diagnostics and effective treatment.
                </p>
              </div>
            </div>
            <div className="col-md-4 col-lg-3">
              <div className="custom-card p-4 rounded shadow-lg" style={{ backgroundColor: '#2a2d3e', color: 'white', border: '1px solid #444', transition: '0.3s' }}>
                <div className="fs-1 mb-3">❤️</div>
                <h3 className="h5 mb-2">Special Care</h3>
                <p className="text-light">
                  Personalized care and attention to every patient to ensure optimal recovery.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Aboutpage;
