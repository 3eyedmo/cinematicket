import './Loading.css';

function Loading() {
  return (
    <div className="cinema-loader">
      <div className="film-reel">
        <div className="reel-left">
          <div className="reel-hole"></div>
          <div className="reel-hole"></div>
          <div className="reel-hole"></div>
        </div>
        <div className="film-strip">
          <div className="film-frame"></div>
          <div className="film-frame"></div>
          <div className="film-frame"></div>
          <div className="film-frame"></div>
        </div>
        <div className="reel-right">
          <div className="reel-hole"></div>
          <div className="reel-hole"></div>
          <div className="reel-hole"></div>
        </div>
      </div>
      <p className="loading-text">Loading cinema rooms...</p>
    </div>
  );
}

export default Loading;